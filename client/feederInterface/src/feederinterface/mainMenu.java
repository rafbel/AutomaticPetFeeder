import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;


public class mainMenu extends JFrame implements ActionListener{
        
	//Widgets
        private JButton feedBtn;
        private JButton addBtn;
        private JButton removeBtn;
        private JButton changeBtn;
        private JButton logoutBtn;
	
	//Objects
	feedCon con = new feedCon();
        
        public mainMenu(){
            
            //Layout
            super("Cat Feeder"); //trocar nome no futuro
            setLayout(null);
            Toolkit tk = Toolkit.getDefaultToolkit();
            int xSize = ((int) tk.getScreenSize().getWidth());
            int ySize = ((int) tk.getScreenSize().getHeight());
            
            setSize(xSize,ySize);
		
	    //Forces the user to login before being able to communicate with the device
		//inserir código aqui
            
	    //botar if -> so aparece os widgets caso o usuario faça o login
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
            
            //Add to layout

        }
        
        public void actionPerformed(ActionEvent event){
		
		if (event.getSource() == feedBtn){ //sends feed message
			//Aparecer option pane para confirmar ou cancelar
			int choice;
			Object[] options = {"Yes", "No"};
			
			choice = JOptionPane.showOptionDialog(null, 
	            		"Are you sure you want to feed your pets?", 
	            		"Choose an option", 
	            		JOptionPane.YES_NO_OPTION, 
	            		JOptionPane.QUESTION_MESSAGE, 
	            		null, 
	            		options, 
	            		options[1]);
			if (choice == 1)
				if (con.sendFeed())
					JOptionPane.showMessageDialog(null, "Your pet was fed! Going back to main menu!");
				else
					JOptionPane.showMessageDialog(null, "We couldn't reach your device right now! Please try again later!");	
					
		}
		if (event.getSource() == addBtn){ //adds a new feed timer
			
		}
		
            
        }
	
        
    
    
}
