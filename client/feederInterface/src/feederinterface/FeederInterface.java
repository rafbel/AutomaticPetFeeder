
package feederinterface;


/**
 *
 * @author Rafael
 */
public class FeederInterface {

    public static void main(String[] args) {
        feedCon con = new feedCon();
        con.login("bellotti.rafael@gmail.com", "med1nho93");
        con.findDevice("feederPi");
        con.getGateway();
        con.connect();
        con.sendFeed();
    }
    
}
