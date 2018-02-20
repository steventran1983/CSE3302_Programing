// Tran, Thang
// 1001-233-804
// 2018-02-18

using System;
using System.IO;
using System.Text.RegularExpressions;

public class hmwk_01
{
    static public void processToken(string token)
    {
        int numInt, notInt = 0, notID = 0, notFP = 0; float numFloat;
        Boolean isInt = int.TryParse(token, out numInt);
        if (isInt)
        {
            Console.WriteLine(">" + token + "< matchs INT");
        }
        else
        {
            notInt++;
        }

        if (token.Contains(".") && !token[0].Equals('.')
           && !token[token.Length - 1].Equals('.'))
        {
            Boolean isFP = float.TryParse(token, out numFloat);
            if (isFP)
            {
                Console.WriteLine(">" + token + "< matchs FP");
            }
            else
            {
                notFP++;
            }
        }
        else
        {
            notFP++;
        }
        if (char.IsLetter(token[0]) || token[0].Equals('_'))
        {
            for (int i = 1; i < token.Length; i++)
            {
                if (!char.IsLetter(token[i]) && !char.IsDigit(token[i])
                    && !token[0].Equals('_'))
                {
                    notID++; break;
                }
                if (i == token.Length - 1)
                {
                    Console.WriteLine(">" + token + "< matchs ID");
                }
            }
        }
        else
        {
            notID++;
        }
        if (notID != 0 && notFP != 0 && notInt != 0)
        {
            Console.WriteLine(">" + token + "<  Does Not Match");
        }
    }

    static public void Main(string[] args)
    {
        //String inputdata = "/Users/thangtran/Projects/homework01/homework01/inputdata.txt";
        Console.WriteLine("processing tokens from " + args[0] + " ...");

        foreach (string line in File.ReadAllLines(args[0]))
        {
            foreach (string token in line.Split((char[])null, StringSplitOptions.RemoveEmptyEntries))
            {
                processToken(token);
            }
        }
    }
}
