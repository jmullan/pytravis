"""
Run the .travis.yml file
"""
import shlex
import yaml
import subprocess
import sys

__version__ = '0.0.1'


def run_scripts(travis, stage):
    """
    Given an travis configuration and a stage, run its scripts if any
    """
    stage_scripts = travis.get(stage, [])
    success = True
    for script in stage_scripts:
        print script
        script_process = subprocess.Popen(
            shlex.split(script),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = script_process.communicate()
        returncode = int(script_process.returncode)
        if returncode > 0:
            sys.stdout.write(out)
            sys.stderr.write(err)
            success = False
    return success


def process(args):
    """
    Do travis stuff
    """
    action_stages = {
        'install': [
            'before_install',
            'install',
            'after_install'
        ],
        'run': [
            'before_script',
            'script',
            'after_script'
        ]
    }

    travis = None
    with open('.travis.yml', 'r') as yaml_file:
        travis = yaml.load(yaml_file)

    # This would be for testing a matrix of environment variables?
    # envs = travis.get('env', [])
    # for env in envs:
    #     print 'setting environment variable', env

    git_options = travis.get('git', {})
    git_submodules = git_options.get('submodules', True)
    if git_submodules:
        print 'initializing and updating git submodules'

    all_success = True
    for action, stages in action_stages.items():
        if action in args.actions:
            for stage in stages:
                success = run_scripts(travis, stage)
                all_success = success and all_success

    if 'run' in args.actions:
        if all_success:
            stage = 'after_success'
        else:
            stage = 'after_failure'
            run_scripts(travis, stage)
