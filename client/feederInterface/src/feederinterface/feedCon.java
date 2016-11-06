/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package feederinterface;

import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.Socket;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.net.ssl.HttpsURLConnection;
import org.json.simple.JSONObject;

/**
 *
 * @author Rafael
 */
public class feedCon {
    
    private String token = "";
    private String deviceUID = "";
    private String proxy = "";
    private int port = 0;
    Socket sock;
    boolean connected = false;
    BufferedReader in;
    PrintWriter out;
    
    public boolean login(String userName, String password){ //logs the user in the weaved service and retrieves token
        try {
            String url = "https://api.weaved.com/v22/api/user/login/"+ userName + "/" + password;
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            
            // optional default is GET
            con.setRequestMethod("GET");
            
            //add request header
            con.setRequestProperty("Content-Type", "application/json");
            
            //add api-key
            con.setRequestProperty("apikey", "WeavedDemoKey$2015");
            
            int responseCode = con.getResponseCode();
            if (responseCode == 404) //not found
                return false;
            
            BufferedReader in = new BufferedReader(
            new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            
            //print result
            String result = response.toString();
            
            Pattern pattern = Pattern.compile("\"token\":\"(.*?)\",");
            Matcher matcher = pattern.matcher(result);
            while (matcher.find()) {
                token = matcher.group(1);
            }
            
            
        } catch (MalformedURLException ex) {
            Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        } catch (ProtocolException ex) {
            Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        } catch (IOException ex) {
            Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }

	
        return true;
    }
    
    public boolean findDevice(String device){ //finds the targeted device among all other devices
        if (token.length() >= 1)
        {
            try {
                String url = "https://api.weaved.com/v22/api/device/list/all";
                URL obj = new URL(url);
                HttpURLConnection con = (HttpURLConnection) obj.openConnection();
                // optional default is GET
                con.setRequestMethod("GET");
                
                //add request header
                con.setRequestProperty("Content-Type", "application/json");
                
                //add api key
                con.setRequestProperty("apikey", "WeavedDemoKey$2015");
                
                //add token
                con.setRequestProperty("token", token);
                
                int responseCode = con.getResponseCode();
                if (responseCode == 404) //not found
                    return false;
               
                
                BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
                String inputLine;
                StringBuffer response = new StringBuffer();
            
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
            
                //print result
                String result = response.toString().substring(1);
                
                Pattern pattern = Pattern.compile("\"devicealias\":\"(.*?)\",");
                Matcher matcher = pattern.matcher(result);
                int counter = -1;
                int deviceIndex = -1;
                while (matcher.find()) {
                    counter++;
                    if (matcher.group(1).equals(device))
                    {
                        deviceIndex = counter;
                        break;
                    }
                }
                if (deviceIndex == -1) //hasn't found device
                    return false;
               
                pattern = Pattern.compile("\"deviceaddress\":\"(.*?)\",");
                matcher = pattern.matcher(result);
                counter = -1;
                while (matcher.find()) {
                    counter++;
                    if (counter == deviceIndex)
                    {
                        deviceUID = matcher.group(1);
                        break;
                    }
                }
                
                
                return true;
                
            } catch (MalformedURLException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            } catch (IOException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            }
        }
        
        return false;
    }
    
    public boolean getGateway(){ //retrieves proxy and port associated with the target device
        if (token.length() >= 1 || deviceUID.length() >= 1)
        {
            try {
                String this_ip = "";
                
                URL oracle = new URL("http://ip.42.pl/raw/");
                BufferedReader br = new BufferedReader(
                new InputStreamReader(oracle.openStream()));

                String inputLine;
                while ((inputLine = br.readLine()) != null)
                    this_ip = inputLine;
                br.close();
                
                String url = "https://api.weaved.com/v22/api/device/connect";
                URL obj = new URL(url);
                HttpURLConnection con = (HttpURLConnection) obj.openConnection();
                // optional default is GET
                con.setRequestMethod("POST");
                
                //add request header
                con.setRequestProperty("Content-Type", "application/json");
                
                //add api key
                con.setRequestProperty("apikey", "WeavedDemoKey$2015"); 
                
                //add token
                con.setRequestProperty("token", token);
                con.setRequestProperty( "charset", "utf-8");
                
                JSONObject sendjson = new JSONObject();
                sendjson.put("deviceaddress", deviceUID);
                sendjson.put("hostip", this_ip);
                sendjson.put("wait", "true");
                //byte[] out = urlParam .getBytes(StandardCharsets.UTF_8);
                // Send post request
		con.setDoOutput(true);
                con.setDoInput(true);
                con.setUseCaches(false);
		DataOutputStream wr = new DataOutputStream(con.getOutputStream());

                wr.write(sendjson.toString().getBytes("UTF-8"));
                
		wr.flush();
		wr.close();
               

		int responseCode = con.getResponseCode();

		BufferedReader in = new BufferedReader(
		new InputStreamReader(con.getInputStream()));
		StringBuffer response = new StringBuffer();

		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();

		//print result
                String access = "";
                String result = response.toString();
                Pattern pattern = Pattern.compile("\"proxy\":\"(.*?)\",");
                Matcher matcher = pattern.matcher(result);
                while (matcher.find()) {
                    access = matcher.group(1);
                }
                int index = access.indexOf(':');
                access = access.substring(index + 5);
                index = access.indexOf(':', index);
                port = Integer.parseInt(access.substring(index + 1));
                proxy = access.substring(0,index);
                
                return true;
            
            } catch (MalformedURLException | ProtocolException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            } catch (IOException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            }

        
    }
        return false;
    }
    
    public int getPort(){return port;}
    public String getProxy(){return proxy;}
    
    public boolean connect()
    {
        if (port != 0 || proxy.length() >= 1)
        {
            try {
                sock = new Socket(proxy,port);
                
                in = new BufferedReader(new
                    InputStreamReader(sock.getInputStream(),"UTF-8"));
                System.out.print("Received string: '");
                String received = "";
                while (!in.ready()) {}
                String line = "";
                while ((line = in.readLine()) != null)
                    received.concat(line);
                System.out.println(received); // Read one line and output it    

                System.out.print("'\n");
                
                //out = new PrintWriter(sock.getOutputStream(), true);
                connected = true;
                
                return true;
            } catch (IOException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            }
        }
        return false;
    }
    
    public boolean close()
    {
        try {
            in.close();
            out.close();
            sock.close();
            
            return true;
        } catch (IOException ex) {
            Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
            return false;
            
        }
    }
    
    public boolean sendFeed() //sends feed command
    {
        if (connected)
        {
            //Sends message to feed
            try {
                out = new PrintWriter(sock.getOutputStream(), true);
                out.print("feed");
                
                //awaits reply 
                BufferedReader in = new BufferedReader(new
                    InputStreamReader(sock.getInputStream()));
                System.out.print("Received string: '");
                String received = "";
                while (!in.ready()) {}
                String line = "";
                while ((line = in.readLine()) != null)
                    received.concat(line);
                System.out.println(received); // Read one line and output it    

                System.out.print("'\n");
                //in.close();
                
                return true;
            } catch (IOException ex) {
                Logger.getLogger(feedCon.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            }
        }
        
        return false;
    }
    
    
}
