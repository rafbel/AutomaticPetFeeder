import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;


public class mainMenu extends JFrame implements ActionListener{
        
        private JButton feedBtn;
        private JButton addBtn;
        private JButton removeBtn;
        private JButton changeBtn;
        private JButton logoutBtn;
        
        public mainMenu(){
            
            //Layout
            super("Cat Feeder"); //trocar nome no futuro
            setLayout(null);
            Toolkit tk = Toolkit.getDefaultToolkit();
            int xSize = ((int) tk.getScreenSize().getWidth());
            int ySize = ((int) tk.getScreenSize().getHeight());
            
            setSize(xSize,ySize);
            
            //Button config:
            feedBtn = new JButton("Feed Now");
            feedBtn.setBounds(0,ySize/5,xSize,100);
            add(feedBtn);
            
            addBtn = new JButton("Add New Feeding Time");
            addBtn.setBounds(0,2*ySize/5,xSize,100);
            add(addBtn);
            
            removeBtn = new JButton("Remove Feeding Time");
            removeBtn.setBounds(0,3*ySize/5,xSize,100);
            add(removeBtn);
            
            changeBtn = new JButton("Change Feeding Time");
            changeBtn.setBounds(0,3*ySize/5,xSize,100);
            add(changeBtn);
            
            

        }
        
        public void actionPerformed(ActionEvent event){
            
        }
	
        
    
    
}