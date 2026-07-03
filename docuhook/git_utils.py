import subprocess
def run_git(args):
    r = subprocess.run(["git"] + args, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None

def get_staged_diff():
    is_repo = run_git(["rev-parse", "--is-inside-work-tree"])
    if is_repo != "true": return None
    return run_git(["diff", "--cached"])
