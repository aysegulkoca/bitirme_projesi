# N-KO

* Proje Ondokuz Mayıs Üniversitesi - Bitirme Projesi kapsamında gerçeklenmiştir. 

N-Ko’nun birincil amacı kullanıcıya kullandığı makine yahut bulunduğu ağ hakkında detaylı, düzenli bir bilgi sunmaktır. Bunu yaparken öncelikli olarak Nmap aracının temel komutları yardımıyla bir tarama işlemi gerçekleştirmektedir. Tarama işlemi arka planda, sırası ile tüm portlara gönderilen SYN paketleri ile gerçekleşmektedir. Araç, aldığı geri dönüşleri değerlendirerek makinenin/makinelerin anlık durumunu (hangi port açık, port üzerinde hangi servis çalışmakta, servisin versiyonu ve varsa ürünü vs.) elde etmektedir. Elde edilen bu parametreler N-Ko tarafından işlenilerek daha düzenli bir hale getirilmektedir ve herhangi bir saldırı uygulamandan, N-Ko’nun içerisinde bulunan veri tabanından portlara ait olası zafiyetler çekilerek listelenmektedir. Tüm bu işlemler, kullanıcının görüşüne hitap etmesi açısından bir rapor sayfasında, tablo altında tutulmaktadır. 

Ek olarak her bir zafiyet için bir risk hesabı yapılmıştır ve elde edilen sonuç, kullanıcının daha net görebilmesi adına rapor sayfasına eklenmiştir. Risk hesabı yapılırken zafiyetlerin sahip olduğu Sömürülebilirlik Alt Skoru (Exploitability Subscore) saldırganın makineye sızabilme ihtimali, Darbe Alt Skoru (Impact Subscore) ise saldırganın sisteme sızdığı zaman verebileceği zarar, şiddet olarak ele alınmıştır. Bu iki puanın çarpımı neticesinde elde edilen sonuç ile zafiyetin yüzdelik olarak ne derece risk taşıdığı bilgisi rapora eklenmiştir.

Listelenen zafiyetler hakkında daha detaylı bilgiye ulaşılmak istendiğinde rapor düzenini bozmaması, sonucu karmaşıklaştırmaması adına zafiyetlerin kendilerine has detay sayfaları oluşturulmuştur. Bu sayfalarda zafiyetin neyden kaynaklandığını açıklayan bir detay kısmı ve zafiyetten korunmak için neler yapılabileceğine dair bir çözüm önerisi kısmı bulunmaktadır.

Uygumalama aynı zamanda, asıl amacının dışında, kullanıcıların sahip olduğu web siteleri hakkında da temel düzeyde bilgi edinebilmelerini amaçlamaktadır. Kullanıcıdan aldığı URL üzerinden basit parametreler yardımıyla SQL Injection ve XSS zafiyetlerinin denemesini yapmaktadır. Bu parametreleri alınan URL’in sonuna eklenmesiyle yeni bir URL oluşturulmaktadır. Oluşturulan yeni URL ile siteye ardışık GET istekleri gönderilmektedir. N-Ko web sitesinden dönen cevapları yorumlayarak elde ettiği sonuçlarla ayrı bir rapor sayfası oluşturmaktadır. 

**GEREKSİNİMLERİ** 

* Python 3.5.0
* Django 2.1.7
