from wav2vec import WavDecoder, CSVFormatter
import os
import csv
import requests
import tarfile
import shutil

ls = ["awb", "bdl", "clb", "jmk", "ksp", "rms", "slt"]

for name in ls:

    print("Downloading", name, "...")

    # Initiate data directory
    if(os.path.isdir("data/") == False): 
        os.mkdir("data")

    # Request and download speaker data
    response = 0

    url = "http://festvox.org/cmu_arctic/cmu_arctic/packed/cmu_us_{}_arctic-0.9{}-release.tar.bz2".format(name, 5)
    response = requests.get(url)

    with open("data/tempZip.tar.bz2", "wb") as code:
        code.write(response.content)

    os.chdir("data")

    # Unzip file 
    tar = tarfile.open("tempZip.tar.bz2", "r:bz2")
    tar.extractall()
    tar.close()
    os.remove("tempZip.tar.bz2")

    if not os.path.exists("in_{}".format(name)):
        os.mkdir("in_{}".format(name))

    # Vectorizing wav file into directory
    for i in range(1,500):
        if(os.path.exists("cmu_us_{}_arctic/wav/arctic_a{:04d}.wav".format(name, i))):
            f = open("in_{}/{}_a{:04d}.csv".format(name, name, i), 'x')
            wd = WavDecoder("cmu_us_{}_arctic/wav/arctic_a{:04d}.wav".format(name, i))
            csvform = CSVFormatter(wd)
            temp = str(csvform)
            f.write(temp)
    for i in range(1, 500):
        if(os.path.exists("cmu_us_{}_arctic/wav/arctic_b{:04d}.wav".format(name, i))):
            f = open("in_{}/{}_b{:04d}.csv".format(name, name, i), 'x')
            wd = WavDecoder("cmu_us_{}_arctic/wav/arctic_b{:04d}.wav".format(name, i))
            csvform = CSVFormatter(wd)
            temp = str(csvform)
            f.write(temp)


    # Make directory for new output data
    shutil.copytree(
        "cmu_us_{}_arctic/lab/".format(name),
        "out_{}/".format(name)
    )

    for i in range(1, 500):
        if(os.path.exists("out_{}/arctic_{:04d}.lab".format(name, i))):
            os.rename(
                "out_{}/arctic_{:04d}.lab".format(name, i),
                "out_{}/{}_{:04d}.csv".format(name, name, i)
            )
    for i in range(1, 500):
        if(os.path.exists("out_{}/arctic_b{:04d}.lab".format(name, i))):
            os.rename(
                "out_{}/arctic_b{:04d}.lab".format(name, i),
                "out_{}/{}_b{:04d}.csv".format(name, name, i)
            )

    print("Speaker", name, "downloaded!")
    os.chdir("../")