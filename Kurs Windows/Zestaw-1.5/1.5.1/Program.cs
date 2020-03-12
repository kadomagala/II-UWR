using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Zestaw_1._5
{
    class Program
    {
        static void Main(string[] args)
        {
            StringBuilder Buffer = new StringBuilder(64);
            int nSize = 64;
            GetUserName(Buffer, ref nSize);
            MessageBox((IntPtr)0, Buffer.ToString(), "Username", 0);
        }

        [DllImport("Advapi32.dll")]
        static extern bool GetUserName(StringBuilder lpBuffer, ref int nSize);

        [DllImport("User32.dll", EntryPoint = "MessageBox", CharSet = CharSet.Auto)]
        public static extern int MessageBox(IntPtr hWnd, string lpText, string lpCaption, uint uType);
    }
}
