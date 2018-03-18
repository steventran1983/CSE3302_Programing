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
        Regex isInt = new Regex(@"^[0-9][0-9]+$");
        Regex isFP = new Regex(@"^[0-9]+[.][0-9]*[1-9]+$");
        Regex isID = new Regex(@"^[A-Za-z_][a-zA-Z0-9_]+$");
        if (isInt.Match(token).Success){
            Console.WriteLine(">" + token + "< matches INT");
        }else if (isFP.Match(token).Success){
            Console.WriteLine(">" + token + "< matches FP");
        }else if (isID.Match(token).Success){
            Console.WriteLine(">" + token + "< matches ID");
        }else{
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


