import time
import multiprocessing
# Adaptação pra rodar no windows
# https://medium.com/@grvsinghal/speed-up-your-python-code-using-multiprocessing-on-windows-and-jupyter-or-ipython-2714b49d6fac
import prog02_f
import concurrent.futures

start = time.perf_counter()

secs = [5,4,3,2,1]

if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as executor:
	 	# f1 = executor.submit(prog02_f.do_something, 1)
	 	# f2 = executor.submit(prog02_f.do_something, 1)
	 	# print(f1.result())
	 	# print(f2.result())
	 	# results = [executor.submit(prog02_f.do_something(sec),sec) for sec in secs ]
	 	# for f in concurrent.futures.as_completed(results):
	 	# 	print(f.result())
	 	results = executor.map(prog02_f.do_something,secs)
	 	for result in results:
	 		print(result)


# processes = []

# if __name__ == '__main__':
# 	for _ in range(10):
# 		p = multiprocessing.Process(target=prog02_f.do_something(1.5))
# 		p.start()
# 		processes.append(p)

# 	for process in processes:
# 		process.join()

	# p1 = multiprocessing.Process(target=prog02_f.do_something())
	# p2 = multiprocessing.Process(target=prog02_f.do_something())

	# p1.start()
	# p2.start()

	# p1.join()
	# p2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')