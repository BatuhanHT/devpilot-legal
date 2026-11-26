# DevPilot Gizlilik Politikası

Son güncelleme: 26 Kasım 2026

DevPilot, yazılım mühendisleri için bir yapay zekâ asistanıdır. Bu politika uygulamanın hangi verileri işlediğini, kimlerle paylaştığını ve bu verileri nasıl silebileceğinizi açıklar.

## Topladığımız veriler

- Hesap verileri: e-posta adresiniz, görünen adınız ve mühendislik rolünüz. Parolanız kimlik doğrulama sağlayıcımız tarafından işlenir ve yalnızca özet (hash) olarak saklanır.
- Oluşturduğunuz içerik: sohbetleriniz ve mesajlarınız, kaydettiğiniz kod parçaları (kod kitaplığı) ve projeleriniz (ad, açıklama, dil ve bağlı repo adresi). Sohbet başlıkları, mesajlar, sohbet özetleri ve kod kitaplığınız saklanmadan önce cihazınızda şifrelenir ("Verilerinizi nasıl koruyoruz" bölümüne bakın).
- Kullanım kayıtları: yapay zekâ isteklerinizin zaman damgaları. Yalnızca istek sınırını uygulamak için tutulur ve bir gün sonra otomatik silinir.
- Giriş güvenliği kayıtları: e-posta ve parolayla giriş yaptığınızda, parola tahminini engellemek için hatalı denemeleri sayarız. E-posta adresinizin kendisini değil, geri döndürülemez bir özetini (hash), hatalı deneme sayısını ve varsa kilidin bitiş zamanını saklarız. Kayıt bir sonraki başarılı girişinizde silinir.
- Yalnızca cihazınızda: uygulama dili seçiminiz ve eklediyseniz GitHub erişim token'ınız (yalnızca bu cihazın iOS Keychain'inde saklanır, sunucularımıza gönderilmez).
- iCloud Anahtar Zincirinizde: kayıtlı sohbetlerinizi koruyan şifreleme anahtarları. Yalnızca kendi Apple cihazlarınız arasında, Apple'ın uçtan uca şifreli iCloud Anahtar Zinciri üzerinden senkronize olur; sunucularımıza gönderilmez.

## Yapay zekâ özellikleri verilerinizi nasıl kullanır

Sohbet ettiğinizde veya kod analizi yaptığınızda DevPilot; mesajınızı, son sohbet geçmişinizi ve eklediğiniz kod ya da repo dosyası içeriğini kendi sunucumuz üzerinden, kullandığımız yapay zekâ servisi NVIDIA NIM'e gönderir. Yanıtlar ancak bu şekilde üretilir. Bu işlem yalnızca vereceğiniz izinle yapılır; izni Profil → Ayarlar → Gizlilik ve Veri bölümünden geri alabilirsiniz.

Uygulama, gönderilecek içeriği önce cihazınızda API anahtarı, token, private key ve parola için tarar. Bulursa size sorar ve varsayılan olarak değeri [REDACTED] ile değiştirir; böylece sır ne yapay zekâ servisine gönderilir ne de saklanır. Bağlı repodaki, genellikle sır içeren dosyalar (ör. .env dosyaları, özel anahtarlar ve sertifikalar) hiç gönderilmez; diğer repo dosyalarında bulunan sırlar otomatik olarak maskelenir.

## Diğer hizmetler

- Supabase: kimlik doğrulamayı ve veritabanımızı barındırır.
- NVIDIA NIM: yapay zekâ yanıtlarını üretir (yukarıya bakın).
- GitHub: bir repo bağlarsanız dosyaları GitHub'dan okunur. Özel repolara kendi token'ınızla, doğrudan cihazınızdan erişilir. Düzenlediğiniz bir dosyayı commit etmeyi seçerseniz, o dosyanın içeriği, commit mesajınız ve GitHub token'ınız doğrudan cihazınızdan GitHub'a gönderilir; hiçbiri sunucularımızdan geçmez. Commit'ler GitHub hesabınız adına yapılır ve GitHub'ın kendi gizlilik koşullarına tabidir.

## Verilerinizi nasıl koruyoruz

- Sohbet başlıkları, mesajlar, sohbet özetleri ve kod kitaplığınız veritabanımıza ulaşmadan önce cihazınızda AES-256-GCM ile şifrelenir. Anahtarlar yalnızca sizin cihazlarınızdadır; bu yüzden ne biz ne de veritabanımıza veya yedeklerimize erişimi olan biri bu içeriği okuyabilir. Size yanıt verebilmek için yapay zekâ servisi, yukarıda anlatıldığı gibi gönderdiğiniz metni okunabilir hâliyle alır.
- Proje adları, açıklamaları ve repo adresleri listelenebilmeleri için bu ek şifreleme olmadan saklanır.
- Tüm trafik şifreli bağlantılar (HTTPS) üzerinden gider ve veritabanımızdaki verilerinize yalnızca kendi hesabınız erişebilir.
- 15 dakika içinde 3 hatalı parola denemesinden sonra o hesaba e-postayla giriş 15 dakika kilitlenir. Apple ve Google ile giriş bundan etkilenmez.
- Uygulamada kopyaladığınız kod yalnızca bu cihazda kalır (Universal Clipboard ile diğer cihazlarınıza geçmez) ve 2 dakika sonra panodan silinir. Uygulama, uygulama değiştiricide içeriğini gizler.

## Yapmadıklarımız

Reklam göstermeyiz, sizi başka şirketlerin uygulama veya sitelerinde izlemeyiz, verilerinizi satmayız; analiz ya da reklam SDK'ları kullanmayız.

## Saklama ve silme

Verileriniz siz silene kadar saklanır. Hesabınızı Profil → Ayarlar → Gizlilik ve Veri → Hesabı sil ile silebilirsiniz. Bu işlem hesabınızı, sohbetlerinizi, mesajlarınızı, kod kitaplığınızı, projelerinizi ve profilinizi sunucularımızdan kalıcı olarak kaldırır ve şifreleme anahtarlarınızı iCloud Anahtar Zincirinizden siler; böylece bir yedekte kalmış olabilecek kopyalar da artık okunamaz. Uygulamayı silmek cihazınızdaki verileri kaldırır.

## Çocuklar

DevPilot 13 yaşından küçük çocuklara yönelik değildir.

## Değişiklikler

Bu politikayı güncelleyebiliriz. Yukarıdaki tarih en son sürümü gösterir.

## İletişim

Bize btemelbusiness@outlook.com adresinden ulaşabilirsiniz.
