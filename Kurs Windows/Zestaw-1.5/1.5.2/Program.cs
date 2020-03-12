using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace _1._5._2
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i = 0; i < 100; i++)
            {
                Console.Out.WriteLine(i + " is " + ((IsPrimeC(i) == 0)?"not prime":"prime")); 
            }

            Console.ReadKey();
        }

        [DllImport("Prime.dll")]
        public static extern int IsPrimeC(int arg);
    }
}
