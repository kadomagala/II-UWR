#include <stdio.h>


extern "C"
{
	__declspec(dllexport) int _stdcall ExecuteC(int n, int(_stdcall *f)(int))
	{
		return (*f)(n);
	}
}