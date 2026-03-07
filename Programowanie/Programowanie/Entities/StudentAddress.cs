using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programowanie.Entities
{
    public class StudentAddress
    {
        public StudentAddress(string city, string street, string homenumber)
        {
            City = city;
            Street = street;
            HomeNumber = homenumber;
        }

        public string City { get; set; }

        public string Street { get; set; }

        public string HomeNumber { get; set; }
    }
}
