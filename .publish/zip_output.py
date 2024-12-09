# create a zip file for the output of the MIKE21HD-Oresund model

import zipfile

zip_fn = ".publish/MIKE21HD-Oresund-output.zip"


def zip_repo():
    with zipfile.ZipFile(zip_fn, "w") as z:
        path_output = "//DKCPH1-STOR.DHI.DK/Projects/11560605/BenchmarkCases/WaterBench-MIKE21HD-Oresund/MIKE21HD-Oresund-output"
        z.write(path_output + "/Area.dfsu")
        z.write(path_output + "/Points.dfs0")
        z.write("README_output.md")
    print(f"Zip file created: {zip_fn}")


if __name__ == "__main__":
    zip_repo()
