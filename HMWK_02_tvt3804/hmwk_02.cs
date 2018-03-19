// Tran, Thang
// 1001-233-804
// 2018-03-10

using System;
using System.IO;
using System.Text.RegularExpressions;

public class hmwk_02
{
    static public void processToken(string token)
    {
        //Defile Regular Expresion 
        Regex isID = new Regex(@"^[a-mN-Z_][n-zA-M0-9_]*$");
        Regex isInt = new Regex(@"^(0d|0D)[0-9]+$");
        Regex isnotEFP = new Regex(@"^[0-9]+$");
        Regex isHexInt = new Regex(@"^(0x|0X)[0-9a-fA-F]+$");
        Regex isFP = new Regex(@"^[0-9]+\.[0-9]+$");
        Regex isEFP = new Regex(@"^(([0-9]+\.)|(\.[0-9]+)|([0-9]+\.[0-9]+)|([0-9]+))([eE][-+]?[0-9]+)?$");

        //Condition to match with RE
        if (isID.Match(token).Success)
        {
            Console.WriteLine(">" + token + "< matches ID.");
        }
        else if (isInt.Match(token).Success)
        {
            Console.WriteLine(">" + token + "< matches INT.");
        }
        else if (isHexInt.Match(token).Success)
        {
            Console.WriteLine(">" + token + "<  matches HEXINT.");
        }
        else if (isFP.Match(token).Success)
        {
            Console.WriteLine(">" + token + "<  matches FP.");
        }
        else if (isnotEFP.Match(token).Success)
        {
            Console.WriteLine(">" + token + "<  does not match.");
        }
        else if (isEFP.Match(token).Success)
        {
            Console.WriteLine(">" + token + "<  matches EFP.");
        }
        else
        {
            Console.WriteLine(">" + token + "<  does not match.");
        }
    }

    static public void Main(string[] args)
    {
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
