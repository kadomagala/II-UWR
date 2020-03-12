using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace _1._5._3
{
    class Program
    {
        static void Main(string[] args)
        {
            MyF myFFromCs = new MyF(IsPrimeCs);
            MyF myFfromC = new MyF(IsPrimeC);

            int number;
            if(Int32.TryParse(Console.ReadLine(), out number))
            {
                Console.Out.WriteLine("Call IsPrimeCS: "+ number + " is " + (ExecuteC(number, myFFromCs) == 0 ? "not prime" : "prime"));
                Console.Out.WriteLine("Call IsPrimeC: " + number + " is " + (ExecuteC(number, myFfromC) == 0 ? "not prime" : "prime"));
            }

            
            Console.ReadKey();


        }

        public delegate int MyF(int n);

        [DllImport("Prime.dll")]
        public static extern int IsPrimeC(int arg);

        [DllImport("ExecuteDll.dll")]
        public static extern int ExecuteC(int arg, MyF f);

        static int IsPrimeCs(int arg)
        {
            if (arg <= 1)
                return 0;
            if (arg == 2 || arg == 3)
                return 1;
            if (arg % 2 == 0 || arg % 3 == 0)
                return 0;
            for (int i = 3; i * i <= arg; i += 2)
            {
                if (arg % i == 0)
                    return 0;
            }
            return 1;
        }
    }
}
