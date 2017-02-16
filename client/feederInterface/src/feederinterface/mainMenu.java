package feederinterface;

import java.awt.Dimension;
import java.awt.Font;
import java.awt.Toolkit;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.Arrays;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

import javax.swing.JList;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.UIManager;
import javax.swing.plaf.FontUIResource;


public class mainMenu extends JFrame implements ActionListener{
        
	//Widgets
        private JButton feedBtn;
        private JButton addBtn;
        private JButton removeBtn;
        private JButton changeBtn;
        private JButton logoutBtn;
        private JList feedList;
        private JScrollPane scroll;
        private String[] timeArray;
	
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
            //UIManager.put("OptionPane.minimumSize",new Dimension(1200,400));
            UIManager.put("OptionPane.font", new Font("yourFontName", Font.BOLD, 30));
            UIManager.put("OptionPane.buttonFont", new FontUIResource(new Font("ARIAL",Font.PLAIN,30)));
            //Button config:
            feedBtn = new JButton("Feed Now");
            feedBtn.setBounds(xSize*2/3,ySize/8,xSize/6,100);
            feedBtn.setFont(new Font("Verdana", Font.BOLD, 32));
            
            addBtn = new JButton("Add New Feeding Time");
            addBtn.setBounds(xSize*2/3,2*ySize/8,xSize/6,100);
            addBtn.setFont(new Font("Verdana", Font.BOLD, 32));
            
            
            removeBtn = new JButton("Remove Feeding Time");
            removeBtn.setBounds(xSize*2/3,3*ySize/8,xSize/6,100);
            removeBtn.setFont(new Font("Verdana", Font.BOLD, 32));
            
            changeBtn = new JButton("Change Feeding Time");
            changeBtn.setBounds(xSize*2/3,4*ySize/8,xSize/6,100);
            changeBtn.setFont(new Font("Verdana", Font.BOLD, 32));
            
            logoutBtn = new JButton("Logout");
            logoutBtn.setBounds(xSize*2/3,5*ySize/8,xSize/6,100);
            logoutBtn.setFont(new Font("Verdana", Font.BOLD, 32));
         
            //JList config
            scroll = new JScrollPane();
            feedList = new JList();
            feedList.setFont(new Font("Verdana", Font.PLAIN, 32));
            scroll.setBounds(xSize/6,ySize/8,xSize/3,ySize*2/3);
            scroll.setViewportView(feedList);
            
		
	    //Forces the user to login before being able to communicate with the device
		//int option = JOptionPane.showMessageDialog(null,null,"Login",JOptionPane.OK_CANCEL_OPTION);
                JTextField fldUser = new JTextField(15);
                JPasswordField fldPass = new JPasswordField(15);
                //fldUser.setPreferredSize( new Dimension( 300, 50 ) );
                fldUser.setFont(new Font("Verdana", Font.PLAIN, 32));
                fldPass.setFont(new Font("Verdana", Font.PLAIN, 32));
                JLabel lblUser = new JLabel("Username:");
                lblUser.setFont(new Font("Verdana", Font.PLAIN, 32));
                JLabel lblPassword = new JLabel("Password:");
                lblPassword.setFont(new Font("Verdana", Font.PLAIN, 32));
                Object[] message = {
                    lblUser, fldUser,
                    lblPassword, fldPass
                };
                
                boolean reqAuth = true;
                while (reqAuth){
                    int result = JOptionPane.showConfirmDialog(null, message, 
                        "Login", JOptionPane.OK_CANCEL_OPTION);
                    if (result == JOptionPane.OK_OPTION){
                        if (feedCon.login(fldUser.getText(),String.valueOf(fldPass.getPassword()))){
                            if (feedCon.findDevice("feederPi")){
                                if (feedCon.getGateway())
                                    if (feedCon.connect()){
                                       reqAuth = false;
                                       populateList();

                                    }
                            }
                        }
                        else{
                            JOptionPane.showMessageDialog(null,
                                "Usuário inválido",
                                "Por favor, tente novamente.",
                                JOptionPane.WARNING_MESSAGE);
                        }
                    }
                    else{
                        
                        this.setVisible(false);
                        this.dispose();
                        reqAuth = false;
                    }
                }

            feedBtn.addActionListener(this);
            addBtn.addActionListener(this);
            removeBtn.addActionListener(this);
            changeBtn.addActionListener(this);
            logoutBtn.addActionListener(this);
            //feedList.addActionListener(this);
            
            add(feedBtn);
            add(addBtn);
            add(removeBtn);
            add(changeBtn);
            add(logoutBtn);
            add(scroll);
            

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
			if (choice == 0)
				if (con.sendFeed()){
                                    JLabel lblReached = new JLabel("Your pet was fed! Going back to main menu!");
                                    lblReached.setFont(new Font("Verdana", Font.PLAIN, 32));
                                    JOptionPane.showMessageDialog(null, lblReached);
                                }
					
                                else{
                                    JLabel lblNotReached = new JLabel("We couldn't reach your device right now! Please try again later!");
                                    lblNotReached.setFont(new Font("Verdana", Font.PLAIN, 32));
					JOptionPane.showMessageDialog(null, lblNotReached);	
                                }	
		}
                else if (event.getSource() == addBtn){ //adds a new feed timer
                    JTextField fldTime = new JTextField(15);
                    fldTime.setFont(new Font("Verdana", Font.PLAIN, 32));
                    JLabel lblTime = new JLabel("Time to be added:");
                    lblTime.setFont(new Font("Verdana", Font.PLAIN, 32));
                    Object[] timeMessage = {
                        lblTime, fldTime,
                    }; 
                    int response = JOptionPane.showConfirmDialog(null, timeMessage, 
                        "Login", JOptionPane.OK_CANCEL_OPTION);
                    if (response == JOptionPane.OK_OPTION){
                        //Checar entrada valida
                        String newTime = fldTime.getText();
                        newTime = newTime.replace(":","");
                        if (con.addTime(newTime)){
                            JOptionPane.showMessageDialog(null, "New feeding time was added! Going back to main menu!");
                            populateList();
                        }
			else
                            JOptionPane.showMessageDialog(null, "We couldn't reach your device right now or the requested feeding time already exists! Please try again later!");	    
                    
                    }
                }
                if (event.getSource() == changeBtn){
                    int index = feedList.getSelectedIndex();
                    if (index == -1){
                       JOptionPane.showMessageDialog(null, "Please select a feeding time to change."); 
                    }
                    else{
                         JTextField fldTime = new JTextField(15);
                         fldTime.setFont(new Font("Verdana", Font.PLAIN, 32));
                         JLabel lblTime = new JLabel("TNew feeding time:");
                        lblTime.setFont(new Font("Verdana", Font.PLAIN, 32));
                        Object[] timeMessage = {
                            lblTime, fldTime,
                        }; 
                        int response = JOptionPane.showConfirmDialog(null, timeMessage, 
                            "Login", JOptionPane.OK_CANCEL_OPTION);
                    if (response == JOptionPane.OK_OPTION){
                        //Checar entrada valida
                        String newTime = fldTime.getText();
                        newTime = newTime.replace(":","");
                        if(con.changeTime(timeArray[index],newTime)){
                            JOptionPane.showMessageDialog(null, "Feeding time was changed! Going back to main menu!");
                            populateList();
                        }
			else
                            JOptionPane.showMessageDialog(null, "We couldn't reach your device right now or the requested feeding time already exists! Please try again later!");
                        }
                            
                    }
                        
                }
                
                if (event.getSource() == removeBtn){
                    int index = feedList.getSelectedIndex(); 
                    if (index == -1){
                       JOptionPane.showMessageDialog(null, "Please select a feeding time to remove."); 
                    }
                    else
                        if(con.removeTime(timeArray[index])){
                            JOptionPane.showMessageDialog(null, "Feeding time was changed! Going back to main menu!");
                            populateList();
                        }
			else
                            JOptionPane.showMessageDialog(null, "We couldn't reach your device right now or the requested feeding time already exists! Please try again later!");
                        
                }
                
                if (event.getSource() == logoutBtn){
                    con.logout();
                    this.setVisible(false);
                    this.dispose();
                }
		
            
        }
        
        private void populateList(){
            timeArray = feedCon.getTimeArray();
            String[] listArray = Arrays.copyOf(timeArray,timeArray.length);
            for (int counter = 0; counter < timeArray.length; counter++){
                StringBuffer sb = new StringBuffer(listArray[counter]);
                sb.insert(listArray[counter].length() - 2, ":");
                listArray[counter] = sb.toString();
            }
            feedList.setListData(listArray);
        }
	
        
    
    
}
