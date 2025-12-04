import subprocess

# TODO: import multiprocessing 

def main(*args, **kwargs):
    for cmd, args in commands.items():
        print(f"Executing command: {cmd} {args}")
        try:
            io_input = [cmd, args]
            result = subprocess.run(
                io_input,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("Command Output:\n", result.stdout)
        except subprocess.CalledProcessError as e:
            print("An error occurred while executing the command:")
            print(e.stderr)


if __name__ == "__main__":

    commands = {
        # runs python processes
        "python3": "python/test_requests.py",

        # runs ruff linters for code quality
        "ruff": "check",

        # runs docker-compose commands for development
        "docker-compose": "build",
        "docker-compose": "up"
    }

    # passes commands into main function
    main(commands)
