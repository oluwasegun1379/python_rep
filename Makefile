#This is a make file

#main:
#	gcc main.c add.c hello.c -o main

$(CC) = gcc
final:
	$(CC) main.c add.c hello.c -o final

Clean:
	rm *.o final
