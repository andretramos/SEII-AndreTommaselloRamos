import time

def do_something(seconds):
	print(f'Sleeping {seconds} second(s)')
	time.sleep(seconds)
	return f'Done Sleeping...{seconds}'