using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zad_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = "Kobyła, ma mały bok.";
            Console.WriteLine(str.IsPalindrome());

            Console.ReadKey();

        }
    }

    public static class StringExtension
    {
        public static bool IsPalindrome(this string str)
        { 
            for(int i = 0, j = str.Length -1 ; i < j; i++, j--)
            {
                while(Char.IsWhiteSpace(str[i]) || Char.IsPunctuation(str[i]))
                {
                    i++;
                }
                while (Char.IsWhiteSpace(str[j]) || Char.IsPunctuation(str[j]))
                {
                    j--;
                }
                if (Char.ToLower(str[i]) != Char.ToLower(str[j]))
                {
                    return false;
                }
            }
            return true;
        }
    }
}
