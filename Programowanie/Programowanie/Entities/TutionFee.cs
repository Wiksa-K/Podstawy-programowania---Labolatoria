using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programowanie.Entities
{
    public class TutionFee
    {
        public TutionFee(decimal amount, bool isPaid, DateTime dueDate)
        {
            Amount = amount;
            IsPaid = false;
            DueDate = dueDate;
        }

        public decimal Amount { get; set; }

        public bool IsPaid { get; set; }

        public DateTime DueDate { get; set; }

        public void Pay()
        {
            IsPaid = true;
        }



    }
}
