using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;

namespace BogusTestApp.Models
{
    public class Order
    {
        public Grid Id { get; set; }
        public DateTime Date { get; set; }
        public decimal OverValue { get; set; }
        public bool Shipped { get; set; }
    }
}
