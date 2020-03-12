#include <stdio.h>


extern "C"
{
	__declspec(dllexport) int _stdcall IsPrimeC(int arg)
	{
		if (arg <= 1)
			return 0;
		if (arg == 2 || arg == 3)
			return 1;
		if (arg % 2 == 0 || arg % 3 == 0)
			return 0;
		for (int i = 3; i * i <= arg; i += 2) {
			if (arg%i == 0)
				return 0;
		}
		return 1;
	}
}