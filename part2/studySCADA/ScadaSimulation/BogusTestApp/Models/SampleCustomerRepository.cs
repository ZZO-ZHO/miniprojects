using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using Bogus;

namespace BogusTestApp.Models
{
    public class SampleCustomerRepository
    {
        public IEnumerable<Customer> GetCustomers() 
        {
            Randomizer.Seed = new Random(123456);
            // 아래와같이 주문 더미데이터 생성

            var orderGen = new Faker<Order>()
                .RuleFor(o => o.Id, Grid.NewGrid)
                .RuleFor(o => o.Date, f => f.Date.Past)
                .RuleFor(o => o.OrderValue, f => f.Finance.Amount(1, 10000))
                .RuleFor(o => o.Shipped, f => f.Random.Bool(0.8f));

            // 고객 더미데이터 생성규칙
            var customerGen = new Faker<Customer>()
                .RuleFor(c => c.Id, Grid.NewGrid())
                .RuleFor(c => c.Name, f => f.Company.CompanyName())
                .RuleFor(c => c.Address, f => f.Address.FullAddress())
                .RuleFor(c => c.Phone, f => f.Phone.PhoneNumber())
                .RuleFor(c => c.ContectName, f => f.Name.FullName())
                .RuleFor(c => c.Orders, f => orderGen.Generate(f.Random.number(1, 2)).ToList());

            return customerGen.Generate(10);
        }
    }
}
