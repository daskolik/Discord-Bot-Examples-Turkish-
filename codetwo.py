import discord
import asyncio
import datetime
import interactions
from discord.ext import commands
import socket   
keyubuvds=socket.gethostname()   
keyubuvdsipadresi=socket.gethostbyname(keyubuvds)   
  
tarihsaat = datetime.datetime.now()
intentts = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True, message_content=True)
client = commands.Bot(command_prefix=':b ', intents=intentts)

bottoken = 'bot token is here'
@client.event
async def on_ready():

    print("__________________________________BOT BİLGİLERİ___________________________________________")
    print("Bot Aktif. Botun Çalıştırıldığı saat ve tarih :", tarihsaat)
    print("token : ", bottoken)
    print("bot isim : {}".format(client.user.name))
    print("bot id : {}".format(client.user.id))
    print("server ip : "+keyubuvdsipadresi)
    print("                                                                  BotInfo by kolik#1337")
    print("______________________________________KONSOL______________________________________________")
    synced = await client.tree.sync() 
    print("[LOG:] SlashCommands Synced : " + str(len(synced)))
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="sınırkapısı")
    await channel.send(f"{member} aramıza katıldı!")
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="sınırkapısı")
    await channel.send(f"{member} aramızdan ayrıldı :( !")



@client.tree.command(name="testslash", description="Haydi! slash komutları herkes test etmeli!")
async def testslash(interaction: discord.Interaction):
    await interaction.response.send_message(content="Başarılı! yakında eklenecek")
@client.tree.command(name="slashawards", description="Haydi! slash komutlarının Public betası üzerine özel rol!")
async def slashawards(interaction: discord.Interaction):
    await interaction.response.send_message(content="Rolü almak için gerekli şartları sağlamıyorsunuz")
@client.command()
async def Kaplumbağalar(ctx):
    print(ctx.message)
    await ctx.send("Kaplumbağa. (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Kaplumbağa (ya da tosbağa), Testudines takımını oluşturan çok sert ve kemiksi bir kabuk içinde yaşayan, ağır yürüyüşlü, dört ayaklı, sürüngenler için kullanılan terim.Hareketleri yönünden ne kadar telaşsız ve ağır hayvanlarsa onların tarih boyunca gelişimi de o kadar yavaş olmuştur. Kaplumbağalar, öteki sürüngenlerle birlikte Mezozoik'in ilk dönemi olan Trias Çağı'nda ortaya çıktılar. 200 milyon yıldan beri kaplumbağaların vücut yapıları önemli hiçbir değişikliğe uğramamıştır. Hâlbuki kaplumbağalar, dünyada soyu henüz tükenmemiş en eski hayvanlardandır.Açlığa pek dayanıklıdırlar. Çok uzun ömürlüdürler. Yüz, yüz elli yıl kadar yaşarlar.Kaplumbağalar çeşitlerine ve yaşadıkları iklim kuşağına göre kış uykusuna yatarlar. Deniz kaplumbağaları kış uykusuna yatmazlar çünkü onlar göç eden hayvanlardır. Bu iç güdünün ortaya çıkmasının nedeni İklim değişikliğidir. Bol Güneş ışığı alan kuru topraklarda kendine bir delik kazıp bütün kışı orada geçirmek üzere içine girer.Günümüzde, soyunu sürdürmekte olan 250'ye yakın kaplumbağa türü bulunmaktadır.")

@client.command()
async def Tavşanlar(ctx):
    print(ctx.message)
    await ctx.send("Tavşanlar. (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Tavşan, Lagomorpha takımı içinde sınıflandırılan tavşangiller (Leporidae) familyasını oluşturan memeli türlerinin ortak adıdır. Yavru bakımları çok azdır. 7 gün baktıktan sonra anne tavşan yavru tavşanı bırakır.Tavşangiller familyası yaklaşık 60 türü içine alır. Kuyrukları uzun kıllarla örtülüdür. Kulaklar ve arka bacaklar uzamıştır. Bir kısmı toprak altında oyuklarda yaşar. Tavşangiller, Ochotonidae familyasını oluşturan pikalardan tüylü küçük kuyrukları, uzun kulakları ve arka ayakları ile ayrılır.Lepus harici cinslerin tüm üyeleri genel olarak ada tavşanı olarak adlandırılır. Ada tavşanları başka hayvanların yuvalarında veya kendi kazdıkları yuvalarda barınırken, tavşanlar uzun ot ve çalıklarda yaşar. Tavşanlar arasında en çarpıcı özelliklere sahip olan beyaz tüylü sera tavşanı 21. yüzyıla damgasını vurmuştur.Ayrıca, bazı türlerin kulakları oldukça iyi duymaktadır. Her türlü sese şaşkınlıkla tepki vermektedirler. Bu yüzden kendi türünden ya da başka canlıların yaklaşması durumunda yabanî tavşanlar irkilirler.Okyanusya hariç tüm yeryüzünde yerlidir. Okyanusya'ya gelişleri yerli memeliler için büyük bir tehdit oluşturur.")

@client.command()
async def Kediler(ctx):
    print(ctx.message)
    await ctx.send("Kediler. (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Evcil kedi[1][4] (Felis catus[4] ya da Felis silvestris catus), küçük, genelde kıllı, evcilleştirilmiş, etobur memeli. Genelde ev hayvanı olarak beslenenlere ev kedisi,[5] ya da diğer kedigillerden ve küçük kedilerden ayırmak gerekmiyorsa kısaca kedi denir. İnsanlar kedilerin arkadaşlığına ve haşarat ev zararlılarını avlayabilme yeteneğine önem vermektedir.Kediler anatomik olarak güçlü, esnek bedenleriyle, hızlı refleksleriyle, keskin, geri çekilebilen pençeleriyle ve küçük avları öldürmeye uyarlanmış dişleriyle diğer kedigillere benzerler. Kediler, insan kulakları için çok zayıf ya da çok yüksek frekanstaki sesleri duyabilirler. Karanlığa yakın ortamlarda görebilirler. Çoğu memeli gibi, kediler insanlara göre daha zayıf renkli görüşe ve daha güçlü koku alma duyusuna sahiptir. **Devamı için https://tr.wikipedia.org/wiki/Kedi adresini ziyaret edebilirsiniz!!!**")


@client.command()
async def Ekremİmamoğlu(ctx):
    print(ctx.message)
    await ctx.send("Ekrem İmamoğlu :white_check_mark: . İstanbul Büyükşehir Belediye Başkanı (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Ekrem İmamoğlu (d. 4 Haziran 1970, Trabzon), Türk siyasetçi ve iş insanıdır. Haziran 2019'dan bu yana İstanbul Büyükşehir Belediye Başkanı olarak görev yapmaktadır.İmamoğlu, 2014-2019 yılları arasında Beylikdüzü Belediye Başkanı olarak görev yaptı. Cumhuriyet Halk Partisi'nden aday gösterildiği 2019 Türkiye yerel seçimlerinde İstanbul Büyükşehir Belediye Başkanı olarak 17 Nisan 2019'da seçimi kazanıp göreve başlasa da, AK Parti'nin itirazları ve Yüksek Seçim Kurulu'nun aldığı kararlar sonucu İstanbul seçimleri iptal edildi. İmamoğlu ise 6 Mayıs 2019'da görevden alındı. 23 Haziran'da yenilenen seçimi de büyük bir halk desteğiyle kazanan İmamoğlu, 27 Haziran 2019 tarihinde mazbatasını alarak göreve başladı.")

@client.command()
async def TOGG_Araba(ctx):
    print(ctx.message)
    await ctx.send("TOGG :white_check_mark: (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Türkiye'nin Otomobili Girişim Grubu veya kısaca Togg, Türkiye merkezli bir otomobil üretici şirkettir. Şirket, fikrî mülkiyet haklarına sahip olduğu ilk otomobilini 29 Ekim 2022 seri üretime hazır hâle geldi. Yapılan bir araştırmaya göre aracın maliyetinin Eylül 2022 itibarıyla 750 bin Türk lirası olduğu tahmin edilmektedir. Aracın satış fiyatının 900 bin Türk lirasının altında olacağı düşünülüyor")

@client.command()
async def chp(ctx):
    print(ctx.message)
    await ctx.send("CHP :white_check_mark: (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Cumhuriyet Halk Partisi, 9 Eylül 1923 tarihinde Mustafa Kemal Atatürk liderliğinde kurulan ve Türkiye'de faaliyet gösteren bir siyasi partidir. Parti tüzüğüne göre resmî kısaltması CHP şeklindedir. Simgesi Altı Ok'tur. TBMM'de 135 milletvekili ile ana muhalefeti temsil eden partidir. Genel başkanı Kemal Kılıçdaroğlu'dur.")

@client.command()
async def KemalKılıçdaroğlu(ctx):
    print(ctx.message)
    await ctx.send("Kemal Kılıçdaroğlu -Ana Muhalefet Partisi Lideri- :white_check_mark: (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Kemal Kılıçdaroğlu (önceki soyadı: Karabulut, d. 17 Aralık 1948 Ballıca, Nazımiye, Tunceli, Türk ekonomist, siyasetçi, bürokrat ve Cumhuriyet Halk Partisinin *CHP genel başkanıdır. 22 Mayıs 2010 tarihinden beri genel başkanlık görevini sürdürmektedir. 2002 ve 2015 yılları arasında yapılan genel seçimlerde İstanbul 2. Bölge Milletvekili olarak Meclis'e girmiştir. Haziran 2015 ve Kasım 2015 genel seçimlerinde İzmir 2. Bölge Milletvekili olarak tekrar Meclis'e girmiştir. 2018 genel seçimlerinde yine İzmir 2. Bölge Milletvekili olarak Meclis'e girmiştir.")

@client.command()
async def MustafaKemalAtatürk(ctx):
    print(ctx.message)
    await ctx.send("Mustafa Kemal Atatürk ☾☆ :white_check_mark: (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Mustafa Kemal Atatürk (1881, Selânik, Osmanlı İmparatorluğu - 10 Kasım 1938, İstanbul, Türkiye), Türk asker ve devlet adamıdır. Türk Kurtuluş Savaşı'nın başkomutanı ve Türkiye Cumhuriyeti'nin kurucusudur.")
    await ctx.send("https://cdn.discordapp.com/attachments/1071848012239884298/1071861167913435146/image.png")

@client.command()
async def mhp(ctx):
    print(ctx.message)
    await ctx.send("Milliyetçi Hareket Partisi (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Milliyetçi Hareket Partisi, 9 Şubat 1969 tarihinde Alparslan Türkeş liderliğinde kurulan ve Türkiye'de etkinlik gösteren siyasi partidir. Parti tüzüğüne göre resmî kısaltması MHP şeklindedir. Simgesi üç hilaldir. TBMM'de 48 milletvekili ile grubu bulunmaktadır. Genel başkanı Devlet Bahçeli'dir.MHP ideoloji olarak; aşırı sağcı, aşırı milliyetçi ve Avrupa şüphecisi bir siyasi partidir. Parti genellikle neo-faşist olarak tanımlanır[20][21][22][23][24] ve bazı şiddet yanlısı paramiliter gruplar[32] ve organize suç örgütleri ile bağlantılıdır. Parti, TBMM'de AKP hükûmetini destekleyen 48 milletvekili ile temsil edilmektedir.")

@client.command()
async def zaferpartisi(ctx):
    print(ctx.message)
    await ctx.send("Zafer Partisi (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Zafer Partisi, 26 Ağustos 2021 tarihinde Ümit Özdağ tarafından kurulan ve Türkiye'de faaliyet gösteren bir siyasi partidir. Ambleminde ay yıldız şeklinde tasarlanan bir meşale vardır. Partinin genel merkezi Çankaya, Ankara'da bulunmaktadır. TBMM'de 1 milletvekili ile temsil edilmektedir.[28] Genel başkanı Ümit Özdağ'dır.Zafer Partisi, bir dönem partinin gençlik kolu olan Ayyıldız Hareketi'nin devamıdır.[29][30] Parti 26 Ağustos 2021 tarihinde İçişleri Bakanlığına kuruluş dilekçesini sunarak resmen kurulmuştur.[31] Parti, ülkedeki göçmenlerin kendi ülkelerine geri gönderilmesini desteklemektedir.[6][7][32]Parti, 2023'te yapılacak olan cumhurbaşkanlığı seçimi için Ankara Büyükşehir Belediye Başkanı Mansur Yavaş'ın aday gösterilmesini istemiştir.[10]")

@client.command()
async def OğuzhanUğur(ctx):
    print(ctx.message)
    await ctx.send("Oğuzhan Uğur - #MevzularAçıkMikrofon (Kaynak wikipedi. Ekleyen admin)")
    await ctx.send("Oğuzhan Uğur, 29 Ocak 1984 tarihinde Hasan Atilla Uğur (Ayrıca Abdullah Öcalan'ın ilk sorgusunu yapan albay Hasan Atilla Uğur'un oğludur.) ve Pakize Uğur'un ilk çocuğu olarak Ankara'da dünyaya geldi. Lise eğitimine önce Ankara Atatürk Anadolu Lisesinde, daha sonra Ankara Bahçelievler Deneme Lisesinde devam etti ve buradan mezun oldu. Akdeniz Üniversitesi Güzel Sanatlar Fakültesi Fotoğraf Bölümünden mezun olan Oğuzhan Uğur, üniversite öğrenciliği sırasında Mustafa Şevki Doğan ve Osman Sınav'ın yardımcılığını yaptı.")
    await ctx.send("**Youtube Kariyeri**")
    await ctx.send("1 Nisan 2017den 23 Temmuz 2017ye kadar Budabi TVde Budabi Haber, Korkoloji, RÖNT ve Budabi Olaylar gibi programlar hazırlamıştır. 12 Ağustos 2017den itibaren kurucusu olduğu BaBaLa TV ye içerik üretmeye başlamıştır. 10 Kasım 2017den 23 Ekim 2020ye kadar Onedio'nun YouTube kanalı için Oğuzhan Uğurla P!NÇ isimli programı hazırlamıştır.Babala TVde RÖNT, Mevzular, Mevzular: Erken Seçim Özel, Oğuzhan Uğurla P!NÇ, Taş-Aşk, Mevzular: Açık Mikrofon gibi programların sunuculuğunu yapmış ve yapmaktadır. 4 Ağustos 2022 tarihinden itibaren BaBaLa TVde yayımlanmaya başlayan ve siyasetçilerin seçmenlerle buluşturulduğu Mevzular: Açık Mikrofon isimli programı büyük beğeni toplamıştır. Programa konuk olarak Ümit Özdağ, Ömer Faruk Gergerlioğlu, Muharrem İnce, Metin Külünk, Cem Uzan ve Ahmet Davutoğlu gibi isimler katılmıştır.Mevzular: Açık Mikrofon, 4 Ağustos 2022 tarihinden itibaren BaBaLa TV'de yayımlanmaya başlayan, moderatörlüğünü Oğuzhan Uğur'un yaptığı siyaset programıdır.")

@client.command()
async def DoğukanAdal(ctx):
    print(ctx.message)
    await ctx.send("Doğukan Adal (Kaynak haberonu&narcobi&nolurbak.com- Ekleyen admin)")
    await ctx.send("Doğukan Adal fenomen, youtuber, twitch yayıncısıdır. 26 Ocak 2001 tarihinde dünyaya geldi. 2017 yılından itibaren yayın yapmaya başlayan Doğukan Adal Youtube ve Twitch hesabından canlı yayınları ve de Minecraft videoları ile tanınmaya başladı. Eğlenceli ve mizahi yönü ile yüz binlerce takipçiye sahiptir.")
    await ctx.send("editörün notu : Genel olarak kaynaklarda Amerika'da doğdudu yazıyor. **Bilginin doğrulundan emin değilim bu yüzden eklemedim.**")

@client.command()
async def OrkunIşıtmak(ctx):
    print(ctx.message)
    await ctx.send("Orkun Işıtmak (Orkuncan Işıtmak) (Kaynak wikipedi- Ekleyen admin)")
    await ctx.send("Orkuncan Işıtmak[1] (d. 8 Ocak 1996; İzmir[2]), Türk YouTuber.[3][4] İstanbul Üniversitesi’nde İtalyan Dili ve Edebiyatı bölümünde okumaktadır. 2012 yılından itibaren eğlence ve oyun içerikli videolar çekmektedir. 2018 yılında İyi Oyun filminde oynadı. 45. Altın Kelebek Ödülleri'nde En iyi YouTuber/Instagrammer Ödülü'nün sahibi oldu.Orkun Işıtmak, 1996 yılında İzmir, Türkiye'de doğdu. Vali Vecdi Gönül Anadolu Lisesi’nden mezun olduktan sonra İstanbul Üniversitesi’ni kazanıp İstanbul’a taşındı fakat daha sonra YouTube’a daha fazla vakit ayırabilmek için eğitimine bir süre ara verdi.[5] 3 Temmuz 2020 tarihinde Netflix'te 1 sezon 15 bölüm yayımlanan, yapımcılığını Acun Medya'nın üstlendiği Exatlon Challenge Türkiye adlı yarışma programında sunuculuk yaptı. Daha önce YouTube’da olan Kirli Çamaşırlar konseptini Acun Ilıcalı’nın kurduğu Exxen adlı platforma taşımıştır.")

@client.command()
async def güvenilirkaynaklar(ctx):
    print(ctx.message)
    await ctx.send("B!Bot Güvenilir Kaynaklar(Ekleyen admin)")
    await ctx.send("Güvenilir Kaynak : Wikipedi / Kararsız Kaynak : /Güvenilir Değil ve Yasaklı :")

@client.command()
async def UtkuCihanYalçınkaya(ctx):
    print(ctx.message)
    await ctx.send("uzielchavo (Utku Cihan Yalçınkaya) Türk Rapçi (Ekleyen admin , kaynak wikipedi)")
    await ctx.send("Utku Cihan Yalçınkaya, 30 Ağustos 1998 yılında İstanbulda dünyaya geldi. Şarkılarında sokak kültürünü çokça yansıtır. Çoğu şarkısında doğduğu ve büyüdüğü semt olan Güngörenden bahseder. Rap müziğe Acil adlı şarkıyla başlamış olsa da geniş kitleler tarafından tanınması 2021 yılında yayınladığı Kan isimli albümünde bulunan Krvn ve Umrumda Değil[1] adlı şarkılar sayesinde olmuştur ve ayrıca albüm 2021 Spotify Top 10 listesinde 10. sırada yer almıştır. 2022 yılında EL CHAVO Albümünü yayınlamıştır.[2][3][4][5] 2022 yılının sonunda Spotifiy üzerinden Türkiye'de en çok dinlenen sanatçı olarak rekor kırıp ayrıca en çok dinlenen ilk iki albümünde sahibi olmuştur 1- EL CHAVO 2- Kan. Böylece Top 5 listesini ele geçirmiş oldu.[6] Bu rekorların ardından Türkiye'nin en önemli ödül törenlerinden biri olan Altın Kelebek'de ödül alamamasına tepki gösterdi.[7]")

@client.command()
async def EnesBatur(ctx):
    print(ctx.message)
    await ctx.send("Enes Batur Sungurtekin (Ekleyen admin , kaynak wikipedi)")
    await ctx.send("Enes Batur Sungurtekin (9 Nisan 1998, Ankara), Türk YouTuber, oyuncu ve şarkıcıdır. Haziran 2021 itibarıyla Türkiye'nin en çok abonesi bulunan bireysel YouTube kanalının sahibidir. Eğlence, video günlüğü ve meydan okuma türü videolar çekmektedir.[1]")

@client.command()
async def GölcükDepremi(ctx):
    print(ctx.message)
    await ctx.send("1999 Gölcük Depremi (Ekleyen admin , kaynak wikipedi)")
    await ctx.send("1999 Gölcük Depremi, İzmit Depremi, Marmara Depremi veya 17 Ağustos 1999 depremi, 17 Ağustos 1999 sabahı, yerel saatle 03.02'de meydana gelen, Kocaeli/Gölcük merkezli deprem. Richter ölçeğine göre 7,6 Mw (USGS, Kandilli Rasathanesi) büyüklüğünde yaşanan deprem, büyük çapta can ve mal kaybına neden olmuştur.")

@client.command()
async def köpekler(ctx):
    print(ctx.message)
    await ctx.send("Köpek(Ekleyen admin , kaynak wikipedi)")
    await ctx.send("Köpek (Canis lupus familiaris[2]); köpekgiller (Canidae) familyasına ait, görünüş ve büyüklükleri farklı 400'den fazla ırkı olan, etçil bir memelidir. Bozkurt'un (C. lupus) alt türlerinden biri olan köpek, tilki ve çakallarla da yakın akrabalardır. Kedilerle birlikte dünyanın en geniş coğrafyaya yayılan ve en çok beslenen iki evcil hayvanından biridir. 2001 yılı tahminlerine göre dünyada 400 milyondan fazla köpek vardır")

@client.command()
async def deprem(ctx):
    print(ctx.message)
    await ctx.send("Deprem(Ekleyen admin , kaynak wikipedi)")
    await ctx.send("Deprem, yer sarsıntısı, seizma veya halk arasında zelzele,[1] yer kabuğunda beklenmedik bir anda ortaya çıkan enerji sonucunda meydana gelen sismik dalgalanmalar ve bu dalgaların yeryüzünü sarsması olayıdır. Sismik aktivite ile kastedilen meydana geldiği alandaki depremin frekansı, türü ve büyüklüğüdür. Depremler sismograf ile ölçülür. Bu olayları inceleyen bilim dalına da sismoloji denir. Depremin büyüklüğü Moment magnitüd ölçeği (ya da eskiden kullanımda olan Richter ölçeği) ile belirlenir. Bu ölçeğe göre 3 ve altı büyüklükteki depremler genelde hissedilmezken 7 ve üstü büyüklükteki depremler yıkıcı olabilir. Sarsıntının şiddeti Mercalli şiddet ölçeği ile ölçülür. Depremin meydana geldiği noktanın derinliği de yıkım kuvvetine etkilidir ve yeryüzüne yakın noktada gerçekleşen depremler daha çok hasar vermektedir.[2]")

@client.command()
async def bibotpartners(ctx):
    print(ctx.message)
    await ctx.send("B!Bot Partner Programı   (Ekleyen admin & son düzenleme 6.02.2023)")
    await ctx.send("B!Bot'un gelişmesinde zaman ve emek harcayan toplulukları desteklemek istiyoruz. Örneğin 25 kişilik sunucunda B!Bot 'u ekledin sunucun gerekli şartları sağlıyorsa seni ortaklık programına davet ederiz.(bu daveti sadece  kolik#1337 yapar)  ve B!Bot Ortaklık Programında olarak sunucuna ve kendine fayda&prestij sağlar.stabil-BETA avantajlarını sunucunda kullanabildiğini bir düşünsene!!")
    await ctx.send("**B!Bot Partner Programına Dahil Kişiler**")
    await ctx.send("**· BraveInn **(discordId : 730493411861463080)")

@client.command()
async def zenci(ctx):
    print(ctx.message)
    await ctx.send("zenci   (Ekleyen admin )")
    await ctx.send("Siyahî ya da zenci antropolojide insanların ayrıldığı ırklardan biri. Bu kavram yalnızca belirli milletleri değil, derileri siyah olan tüm insanları kapsar. Batılı devletlerde yaygın olarak kullanılan Afro (Afrikalı) ve Karayipli sözcükleri de zaman zaman Türkçede kullanılır.")

@client.command()
async def discord(ctx):
    print(ctx.message)
    await ctx.send("Discord    (Ekleyen admin )")
    await ctx.send("Discord, topluluk kurma için tasarlanmış bir anlık mesajlaşma ve dijital dağıtım platformudur. Aralık 2020 tarihi itibarıyla 300 milyondan fazla kayıtlı kullanıcısı ve aylık 140 milyon aktif kullanıcısı vardır.[2] Discord Windows, macOS, Linux, iOS, Android ve Web tarayıcısı üzerinde çalışabilmektedir..")

@client.command()
async def discordtürkiye(ctx):
    print(ctx.message)
    await ctx.send("Discord Türkiye (Ekleyen admin )")
    await ctx.send("Discord Türkiye, Türk Discord kullanıcılarının sohbet edebileceği forum platformudur.")

@client.command()
async def minecraft(ctx):
    print(ctx.message)
    await ctx.send("Discord Türkiye (Ekleyen admin )")
    await ctx.send("Discord Türkiye, Türk Discord kullanıcılarının sohbet edebileceği forum platformudur.")

@client.command()
async def asdfasd(ctx):
    print(ctx.message)
    await ctx.send("asdfasd")
    await ctx.send("babapro")



client.run(bottoken)
