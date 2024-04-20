using System.Diagnostics;

namespace VK;

internal abstract class Program
{
    private static void Main()
    {
        try
        {
            while (true)
            {
                Console.WriteLine("\n1. Show all running processes");
                Console.WriteLine("2. Kill a process by its ID");
                Console.WriteLine("3. Quit\n");
                
                Console.Write("Enter your choice: ");
                var choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        PrintProcesses();
                        break;
                    case "2":
                        Console.Write("Enter the process ID: ");

                        var processId = Console.ReadLine();
                        if (processId is null)
                        {
                            Console.WriteLine("Process ID cannot be null.");
                            break;
                        }

                        KillProcess(processId);
                        break;
                    case "3":
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
    }

    private static void PrintProcesses()
    {
        foreach (var process in Process.GetProcesses())
        {
            Console.WriteLine($"ID: {process.Id}; Name: {process.ProcessName}");
        }
    }

    private static void KillProcess(string processId)
    {
        try
        {
            if (int.TryParse(processId, out var id))
            {
                var process = Process.GetProcessById(id);
                process.Kill();
                Console.WriteLine($"Process with ID {processId} has been terminated.");
            }
            else
            {
                Console.WriteLine("Process ID must be a number.");
            }
        }
        catch (ArgumentException)
        {
            Console.WriteLine($"Process with ID {processId} is not found.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
    }
}