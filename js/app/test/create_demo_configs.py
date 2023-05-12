import os
import subprocess

snapshots_dir = os.path.join(os.path.dirname(__file__), "../snapshots")

demo_names = {
    f.split(".")[0]
    for f in os.listdir(os.path.dirname(__file__))
    if ".spec.ts" in f
}
for f in os.listdir(snapshots_dir):
    if ".spec.ts" in f and not os.path.isdir(os.path.join(snapshots_dir, f)):
        demo_names.add(f.split(".")[0])


for demo in demo_names:
    print(f"Generating demo: {demo}")
    command = (
        f"python ../../../demo/write_config.py {demo} ../../../demo/{demo}/config.json"
    )
    process = subprocess.Popen(
        command.split(), stdout=subprocess.PIPE, cwd=os.path.dirname(__file__)
    )
    output, error = process.communicate()
