CC = gcc

all:fib.o
	$(CC) -o fib fib.o

c.o:
	$(CC) -c $<

install:
	mkdir -p /usr/bin
	cp fib /usr/bin
	chmod 755 /usr/bin/fib
