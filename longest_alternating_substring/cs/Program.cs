using System;
using System.Linq;
using System.Collections.Generic;

namespace substring
{
    class Program
    {
        static void Main(string[] args)
        {
            var res = longest_substring("225424272163254474441338664823");
            System.Console.WriteLine(res);

        }

        public static string longest_substring(string digits){

            var numbers = new List<int>();
            for (var i=0; i<digits.Length; i++){
                var num = (int)(digits[i] - '0');
                numbers.Add(num % 2);
            }

            var idx_lst = new List<List<int>>();
            for (var i=1; i<numbers.Count; i++){
                var arr = new int[] { numbers[i-1], numbers[i] };

                if (arr.SequenceEqual(new int[] {0, 1}) || 
                    arr.SequenceEqual(new int[] {1, 0})){
                    idx_lst.Add(new List<int>{i-1, i});
                }
            }

            var c = 0;
            while (c < idx_lst.Count-1){
                 
                if (idx_lst[c].Last() == idx_lst[c+1].First()){
                    idx_lst[c+1].RemoveAt(0);
                    idx_lst[c].Add(idx_lst[c+1][0]);
                    idx_lst.RemoveAt(c+1);
                    continue;
                }

                c += 1;
            }


            var substring = new List<String>();
            foreach (var i in idx_lst)
            {
                var txt = "";
                foreach (var j in i)
                {
                    txt += digits[j].ToString();
                }
                substring.Add(txt);
            }

            var len_substring = new List<int>();
            foreach(var i in substring){
                len_substring.Add(i.Length);
            }
            var max_idx = len_substring.IndexOf(len_substring.Max());

            return substring[max_idx];
        }
    }
}
