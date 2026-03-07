// See https://aka.ms/new-console-template for more information

using Programowanie.Entities;

Student student = new Student("Wiksa Kurowska", 17, "222-222-222");

StudentAddress adres = new StudentAddress("Rzeszów", "Zagorzyce", "409A");

student.AddCourse(1,"Programowanie");
student.AddCourse(2,"Bazy danych");
student.AddCourse(3,"Polityka");

student.AddGrade(1, 5);
student.AddGrade(2, 5);
student.AddGrade(3, 5);

student.Pay(940);
student.Pay(940);

Console.WriteLine("Imię nazwisko: " + student.FullName);
Console.WriteLine("Wiek: " + student.Age);
Console.WriteLine("Nr Tel.: " + student.PhoneNumber);

Console.WriteLine("Status: " + student.Status);

Console.WriteLine("Miasto: " + adres.City);
Console.WriteLine("Ulica: " + adres.Street);
Console.WriteLine("Nr domu: " + adres.HomeNumber);

Console.WriteLine("Lista przedmiotów: ");
foreach(Course item in student.Courses)
{
    Console.WriteLine(item.Name + " ocena: " + item.Grade );
}

Console.WriteLine("Czesne");

foreach(TutionFee item in student.TutionFees)
{
    Console.WriteLine(item.DueDate + " Zapłacono: " + item.IsPaid + " Kwota: " + item.Amount);
}



Console.WriteLine("Hello, World!");
