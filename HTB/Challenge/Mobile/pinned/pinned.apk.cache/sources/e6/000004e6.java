package com.example.pinned;

import android.os.Bundle;
import android.os.StrictMode;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import b.b.c.j;
import c.b.a.c;
import c.b.a.d;
import c.b.a.e;
import c.b.a.f;
import c.b.a.g;
import c.b.a.h;
import c.b.a.i;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.KeyStore;
import java.security.cert.Certificate;
import java.security.cert.CertificateFactory;
import java.util.ArrayList;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;

/* loaded from: classes.dex */
public class MainActivity extends j {
    public String o = "";
    public Certificate p = null;
    public SSLContext q = null;
    public TextView r = null;
    public TextView s = null;
    public TextView t = null;
    public Button u = null;

    /* loaded from: classes.dex */
    public class a implements View.OnClickListener {
        public a() {
        }

        @Override // android.view.View.OnClickListener
        public void onClick(View view) {
            MainActivity.this.r.setText("");
            try {
                MainActivity.this.w();
                MainActivity.this.x();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    /* loaded from: classes.dex */
    public class b implements Runnable {

        /* renamed from: b  reason: collision with root package name */
        public final /* synthetic */ HttpsURLConnection f1023b;

        /* loaded from: classes.dex */
        public class a implements Runnable {

            /* renamed from: b  reason: collision with root package name */
            public final /* synthetic */ String f1025b;

            public a(String str) {
                this.f1025b = str;
            }

            @Override // java.lang.Runnable
            public void run() {
                MainActivity.this.r.setText(this.f1025b);
            }
        }

        public b(HttpsURLConnection httpsURLConnection) {
            this.f1023b = httpsURLConnection;
        }

        @Override // java.lang.Runnable
        public void run() {
            try {
                StringBuilder sb = new StringBuilder();
                sb.append(this.f1023b.getResponseCode());
                sb.append(" ");
                sb.append(this.f1023b.getResponseMessage());
                sb.append("\n");
                Certificate[] serverCertificates = this.f1023b.getServerCertificates();
                for (Certificate certificate : serverCertificates) {
                    if (!MainActivity.this.p.toString().equals(serverCertificates[0].toString())) {
                        throw new Exception("Connection is not honoured as the bundled certificate does not match the certificate data in the incoming request.");
                    }
                    MainActivity.super.runOnUiThread(new a(MainActivity.u(MainActivity.this, this.f1023b)));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static String u(MainActivity mainActivity, HttpURLConnection httpURLConnection) {
        mainActivity.getClass();
        StringBuilder sb = new StringBuilder();
        if (httpURLConnection != null) {
            try {
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
                while (true) {
                    String readLine = bufferedReader.readLine();
                    if (readLine == null) {
                        break;
                    }
                    sb.append(readLine);
                    System.out.println(readLine);
                }
                bufferedReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return sb.toString();
    }

    @Override // b.k.b.p, androidx.activity.ComponentActivity, b.h.b.f, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder().permitAll().build());
        this.s = (TextView) findViewById(R.id.editTextTextPersonName);
        this.t = (TextView) findViewById(R.id.editTextTextPassword2);
        this.r = (TextView) findViewById(R.id.textView3);
        Button button = (Button) findViewById(R.id.button);
        this.u = button;
        button.setOnClickListener(new a());
    }

    public void w() {
        this.p = CertificateFactory.getInstance("X.509").generateCertificate(getResources().openRawResource(R.raw.certificate));
        KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
        keyStore.load(null, null);
        keyStore.setCertificateEntry("Self signed certificate", this.p);
        TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        trustManagerFactory.init(keyStore);
        SSLContext sSLContext = SSLContext.getInstance("TLS");
        this.q = sSLContext;
        sSLContext.init(null, trustManagerFactory.getTrustManagers(), null);
    }

    public void x() {
        HttpsURLConnection httpsURLConnection;
        TextView textView;
        String str;
        MainActivity mainActivity = this;
        HttpsURLConnection httpsURLConnection2 = (HttpsURLConnection) new URL("https://pinned.com:443/pinned.php").openConnection();
        httpsURLConnection2.setRequestMethod("POST");
        httpsURLConnection2.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        httpsURLConnection2.setRequestProperty("Accept", "application/x-www-form-urlencoded");
        httpsURLConnection2.setRequestProperty("charset", "utf-8");
        httpsURLConnection2.setDoOutput(true);
        httpsURLConnection2.setSSLSocketFactory(mainActivity.q.getSocketFactory());
        if (mainActivity.s.getText().toString().equals("bnavarro") && mainActivity.t.getText().toString().equals("1234567890987654")) {
            StringBuilder g = c.a.a.a.a.g("uname=bnavarro&pass=");
            StringBuilder sb = new StringBuilder();
            sb.append(d.a());
            sb.append(c.b.a.b.a());
            sb.append(h.a());
            sb.append(c.a());
            sb.append(i.a());
            ArrayList arrayList = new ArrayList();
            arrayList.add("9GDFt6");
            arrayList.add("83h736");
            arrayList.add("kdiJ78");
            arrayList.add("vcbGT6");
            arrayList.add("LPGt63");
            arrayList.add("kFgde4");
            arrayList.add("5drDr4");
            arrayList.add("Y6ttr5");
            arrayList.add("444w45");
            arrayList.add("hjKd56");
            sb.append((String) arrayList.get(4));
            sb.append(e.a());
            sb.append(f.a());
            ArrayList arrayList2 = new ArrayList();
            arrayList2.add("TG7ygj");
            arrayList2.add("U8uu8i");
            arrayList2.add("gGtT56");
            arrayList2.add("84hYDG");
            arrayList2.add("yRCYDm");
            arrayList2.add("7ytr4E");
            arrayList2.add("j5jU87");
            arrayList2.add("yRCYDm");
            arrayList2.add("jd9Idu");
            arrayList2.add("kd546G");
            sb.append((String) arrayList2.get(7));
            sb.append(c.b.a.a.a());
            String sb2 = sb.toString();
            char charAt = b.q.h.b().charAt(3);
            char charAt2 = b.q.h.b().charAt(0);
            char charAt3 = c.a().charAt(0);
            char charAt4 = c.b.a.a.a().charAt(8);
            char charAt5 = h.a().charAt(1);
            char charAt6 = b.q.h.b().charAt(0);
            char charAt7 = i.a().charAt(5);
            char charAt8 = c.b.a.a.a().charAt(7);
            char charAt9 = c.b.a.b.a().charAt(4);
            httpsURLConnection = httpsURLConnection2;
            char charAt10 = e.a().charAt(4);
            char charAt11 = e.a().charAt(4);
            char charAt12 = i.a().charAt(5);
            char charAt13 = d.a().charAt(3);
            char charAt14 = d.a().charAt(5);
            char charAt15 = h.a().charAt(1);
            char charAt16 = h.a().charAt(1);
            SecretKeySpec secretKeySpec = new SecretKeySpec((String.valueOf(charAt) + String.valueOf(charAt2) + String.valueOf(charAt3) + String.valueOf(charAt4).toUpperCase() + String.valueOf(charAt5) + String.valueOf(charAt6) + String.valueOf(charAt7).toUpperCase() + String.valueOf(charAt8) + String.valueOf(charAt9) + String.valueOf(charAt10) + String.valueOf(charAt11) + String.valueOf(charAt12).toUpperCase() + String.valueOf(charAt13) + String.valueOf(charAt14) + String.valueOf(charAt15) + String.valueOf(charAt16)).getBytes(), g.a());
            Cipher cipher = Cipher.getInstance(g.a());
            cipher.init(2, secretKeySpec);
            g.append(new String(cipher.doFinal(Base64.decode(sb2, 0)), "utf-8"));
            mainActivity = this;
            mainActivity.o = g.toString();
            textView = mainActivity.r;
            str = "You are logged in.";
        } else {
            httpsURLConnection = httpsURLConnection2;
            StringBuilder g2 = c.a.a.a.a.g("uname=");
            g2.append(mainActivity.s.getText().toString());
            g2.append("&pass=");
            g2.append(mainActivity.t.getText().toString());
            mainActivity.o = g2.toString();
            textView = mainActivity.r;
            str = "Wrong credentials!";
        }
        textView.setText(str);
        DataOutputStream dataOutputStream = new DataOutputStream(httpsURLConnection.getOutputStream());
        try {
            dataOutputStream.writeBytes(mainActivity.o);
            dataOutputStream.flush();
            dataOutputStream.close();
            new Thread(new b(httpsURLConnection)).start();
        } finally {
        }
    }
}