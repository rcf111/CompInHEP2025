import multiprocessing
import subprocess

MAX_WORKERS = max(multiprocessing.cpu_count()-1,1)

n=10

def runthatfiledude(nimi,i):
    with open(f"output_py_{i}.txt", "w") as f:
        subprocess.run(["./runnable", str(i)], stdout=f)

def main():
    pool = multiprocessing.Pool(MAX_WORKERS)
    for i in range(n):
        p = multiprocessing.Process(target=runthatfiledude, args=("protsess",i+1))
        p.start()

#heavy help from chatgpt on the last two


if __name__ == "__main__":
    main()
