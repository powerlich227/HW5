CFLAGS = -shared
LIBS = -lm
CC = gcc

all: libhmwk5p2

diffusion.o:	diffusion.c diffusion.h
	$(CC) $(CFLAGS)	-fpic -c diffusion.c

libhmwk5p2:	diffusion.o
	$(CC) $(CFLAGS) $(LIBS) -o libhmwk5p2.so diffusion.o

clean:
	rm -f *.o libhmwk5p2
