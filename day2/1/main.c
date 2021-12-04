#include <stdio.h>
#include <stdlib.h>

int nextBytesAsciiValue(FILE *file);

int main() {
	int forward = 0;
	int depth = 0;
	FILE *file = fopen("input.txt", "rb");
	if (file == NULL) {
		return 1;
	}

	int cmd = 0;
	do { 
	    cmd = fgetc(file);
	    if (cmd == 'f') {
		    // <f>orward X ->
		    // forward 7 bytes to get to position of <X>
		    fseek(file, 7, SEEK_CUR);
		    forward += nextBytesAsciiValue(file);
	    } else if (cmd == 'd') {
		    // <d>own X ->
		    // forward 4 bytes to get to position of <X>
		    fseek(file, 4, SEEK_CUR);
		    depth += nextBytesAsciiValue(file);
	    } else if (cmd == 'u') {
		    //<u>p X ->
		    // forward 2 bytes to get to position of <X>
		    fseek(file, 2, SEEK_CUR);
		    depth -= nextBytesAsciiValue(file);
	    } 
	} while (cmd != EOF);

	fclose(file);
	printf("You moved forward: %d units of distance.\n", forward);
	printf("You are at a depth of %d units of distance.\n", depth);
	printf("The product of these values is %d\n.", forward*depth);
	return 0;
}

int nextBytesAsciiValue(FILE *file) {
	return abs(48 - fgetc(file));
}
