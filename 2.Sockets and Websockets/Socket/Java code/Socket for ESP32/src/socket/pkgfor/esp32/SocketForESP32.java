package socket.pkgfor.esp32;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author ed000
 */
public class SocketForESP32 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(699);
            System.out.println("[*] Server iniciado, esperando conexión del ESP32...");
            Socket esp32 = server.accept();
            System.out.println("[*] ESP32 conectado!");
            BufferedReader entrada = new BufferedReader(new InputStreamReader(esp32.getInputStream()));
            System.out.println("[*] ESP32 dice: "+entrada.readLine());
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
        
    }
    
}
