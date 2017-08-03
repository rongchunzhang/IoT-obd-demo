TARGET = ../C/carserver
OBJS = car_server.o 
CC = gcc
CFLAGS =

$(TARGET): $(OBJS)
	$(CC) -Wall -ggdb $(OBJS) -L. -o $(TARGET) -lwiringPi

%.o: %.c
	$(CC) -c $(CFLAGS) $< -o $@  -lwiringPi

test: $(OBJS)
	$(CC) -Wall -ggdb $(OBJS) -L. -o $(TARGET) -lwiringPi

clean:
	rm -f $(OBJS)
	rm -f $(TARGET)
