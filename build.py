#!/usr/bin/python3

import subprocess

process = subprocess.run(["cargo", "search", "mdbook"], check=True, capture_output=True)
for line in process.stdout.decode().splitlines():
    package, _, version, _ = line.split(" ", 3)
    if package == "mdbook":
        break

version = version.strip('"')
subprocess.run(
    [
        "docker",
        "build",
        "-t",
        "thefarwind/mdbook:latest",
        "-t",
        f"thefarwind/mdbook:{version}",
        "--build-arg",
        f"MDBOOK_VERSION={version}",
        ".",
    ],
    check=True,
)

subprocess.run(
    ["docker", "push", "thefarwind/mdbook:latest"], check=True,
)

subprocess.run(
    ["docker", "push", f"thefarwind/mdbook:{version}"], check=True,
)
