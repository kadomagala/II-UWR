using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zad1
{
    class Program
    {
        static void Main(string[] args)
        {
            int liczbaProb = 100000;

            ArrayList arrayList = new ArrayList();
            List<int> list = new List<int>();

            DateTime start = DateTime.Now;

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                arrayList.Add(i);

            }
            DateTime end = DateTime.Now;
            TimeSpan timeSpan = end - start;
            Console.Out.WriteLine("Czas dodawania do ArrayList: {0}", timeSpan);



            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                list.Add(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas dodawania do List<T> : {0}", timeSpan);

            int sum = 0;
            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                sum += arrayList.IndexOf(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas przegladania ArrayList : {0}", timeSpan);


            sum = 0;
            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                sum += list.IndexOf(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas przegladania List<T> : {0}", timeSpan);

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                arrayList.Remove(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas usuwania z ArrayList: {0}", timeSpan);

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                list.Remove(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas usuwania z List<T>: {0}", timeSpan);

            Console.ReadKey();

            Hashtable hashtable = new Hashtable();
            Dictionary<int, int> dict = new Dictionary<int, int>();

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                hashtable.Add(i, -i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas dodawania do Hashtable : {0}", timeSpan);

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                dict.Add(i, -i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas dodawania do Dictionary<int,int> : {0}", timeSpan);
            Console.ReadKey();

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                Console.Out.WriteLine(hashtable[i]);
            }
            end = DateTime.Now;
            timeSpan = end - start;


            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                Console.Out.WriteLine(dict[i]);
            }
            end = DateTime.Now;
            Console.Out.WriteLine("Czas przegladania Hashtable : {0}", timeSpan);
            timeSpan = end - start;
            Console.Out.WriteLine("Czas przegladania Dictionary<int,int>: {0}", timeSpan);

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                hashtable.Remove(i);
                
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas usuwania z Hashtable : {0}", timeSpan);

            for (int i = 0; i < liczbaProb; i++)
            {
                if (i == 50) start = DateTime.Now;
                dict.Remove(i);
            }
            end = DateTime.Now;
            timeSpan = end - start;
            Console.Out.WriteLine("Czas usuwania z Dictionary<int, int> : {0}", timeSpan);
            Console.ReadKey();
        }
    }
}

