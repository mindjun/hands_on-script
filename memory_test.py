import platform
import resource
import sys


def memory_limit(percentage: float):
    """
    只在linux操作系统起作用
    """
    if platform.system() != "Linux":
        print('Only works on linux!')
        return
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    print(soft, hard)
    # resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
    resource.setrlimit(resource.RLIMIT_AS, (1024 * 4, 1024 * 6))


def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory


def memory(percentage=0.8):
    def decorator(function):
        def wrapper(*args, **kwargs):
            memory_limit(percentage)
            try:
                function(*args, **kwargs)
            except MemoryError:
                mem = get_memory() / 1024 / 1024
                print('Remain: %.2f GB' % mem)
                sys.stderr.write('\n\nERROR: Memory Exception\n')
                sys.exit(1)

        return wrapper

    return decorator


@memory(percentage=0.8)
def main():
    store = {}
    for i in range(10000):
        store[str(i)] = 'My memory is limited to 80%.'
    print(len(store))


if __name__ == '__main__':
    main()
