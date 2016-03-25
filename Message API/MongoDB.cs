using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace mongoDB
{
    class Program
    {
        static void Main(string[] args)
        {
            // Demo for list
            var notification = new Notification();
            List<Notification> notifications =  notification.notificationList();

           // notifications.Count();


            //Demo set flag
            ObjectId Id = notifications.First().Id;
            Notification.sent_message(Id).Wait();
        
        }

        public class Notification
        {
            public ObjectId Id { get; set; }
            public string body { get; set; }
            public bool sent_flag { get; set; }
            public DateTime date { get; set; }

            // function returns a list of unsent messages.
            public List<Notification> notificationList() {
                // Main logic
                var client = new MongoClient("mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1");
                var db = client.GetDatabase("stockadvisordb");
                var col = db.GetCollection<Notification>("notifications");

                var notifications = col
                    .Find(notification => notification.sent_flag == false)
                    .ToListAsync()
                    .Result;


                foreach (var notification in notifications)
                {
                    Console.WriteLine("{");
                    Console.WriteLine(notification.Id);
                    Console.WriteLine(notification.body);
                    Console.WriteLine(notification.date);
                    Console.WriteLine("}");
                }

                return notifications;
            }


           public static async Task sent_message(ObjectId Id)
            {

                var client = new MongoClient("mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1");
                var db = client.GetDatabase("stockadvisordb");
                var col = db.GetCollection<Notification>("notifications");

                var updateFilter = Builders<Notification>.Filter.Eq("_id", Id);
                var update = Builders<Notification>.Update.Set("sent_flag", true);

                await col.UpdateOneAsync(updateFilter, update);
            }
        }
    }
}
