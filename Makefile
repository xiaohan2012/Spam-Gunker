chn_parser: chn_parser.cpp ICTCLAS50.h
	 g++ -g chn_parser.cpp ./libICTCLAS50.so  -m32  -O3 -DOS_LINUX -o chn_parser
clean:
	rm chn_parser
