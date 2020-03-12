#include <Windows.h>
#include <stdio.h>
#include <Shlobj.h>


int main()
{
	wchar_t desktop[MAX_PATH];
	if (SUCCEEDED(SHGetFolderPathW(NULL, CSIDL_DESKTOP | CSIDL_FLAG_CREATE, NULL, 0, desktop)))
	{

		wchar_t filename[MAX_PATH];
		swprintf_s(filename, MAX_PATH, L"%s\\%s", desktop, L"file.txt");

		FILE *fp;
		_wfopen_s(&fp, filename, L"w");
		if (fp)
		{
			SYSTEMTIME st;

			GetSystemTime(&st);

			fprintf(fp, "%02d - %02d - %02d %02d:%02d:%02d", st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond);
			fclose(fp);
			ShellExecute(NULL, (LPCWSTR)L"print", filename, NULL, NULL, SW_NORMAL);
		}
		else
		{
			wprintf(L"can't create file\n");
		}

	}

	return 0;
}