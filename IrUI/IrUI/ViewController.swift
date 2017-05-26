//
//  ViewController.swift
//  IrUI
//
//  Created by Antonis Vozikis on 26/05/2017.
//  Copyright © 2017 Antonis Vozikis. All rights reserved.
//

import UIKit
import Foundation

class ViewController: UIViewController {

    @IBOutlet weak var textView: UITextField!
    @IBOutlet weak var googleButton: UIButton!
    @IBOutlet weak var yahooButton: UIButton!
    @IBOutlet weak var bingButton: UIButton!
    var google = "0"
    var yahoo = "0"
    var bing = "0"
    let pathQuery = "Users/tony/Developer/Python/irQuery.txt"
    let pathEngines = "Users/tony/Developer/Python/irEngines.txt"
    

    override func viewDidLoad() {
        super.viewDidLoad()
        googleButton.setTitleColor(UIColor.red, for: .normal)
        yahooButton.setTitleColor(UIColor.red, for: .normal)
        bingButton.setTitleColor(UIColor.red, for: .normal)
        googleButton.setTitleColor(UIColor.red, for: .normal)
        googleButton.setTitleColor(UIColor.red, for: .normal)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    @IBAction func clearFunc(_ sender: Any) {
        googleButton.setTitleColor(UIColor.red, for: .normal)
        google = "0"
        yahooButton.setTitleColor(UIColor.red, for: .normal)
        yahoo = "0"
        bingButton.setTitleColor(UIColor.red, for: .normal)
        bing = "0"
        textView.text = nil
    }
    
    @IBAction func googleFunc(_ sender: Any) {
        googleButton.setTitleColor(UIColor.gray, for: .normal)
        google = "1"
    }

    @IBAction func yahooFunc(_ sender: Any) {
        yahooButton.setTitleColor(UIColor.gray, for: .normal)
        yahoo = "1"
    }
    
    @IBAction func bingFunc(_ sender: Any) {
        bingButton.setTitleColor(UIColor.gray, for: .normal)
        bing = "1"
    }
    @IBAction func send(_ sender: Any) {
        if let text = textView.text {
                do {
                    try text.write(toFile: pathQuery, atomically: false, encoding: String.Encoding.utf8)
                    
                }
                catch {print("Cant write data to IrQuery.txt")}
                let GYB = google + yahoo + bing
                do {
                    try GYB.write(toFile: pathEngines, atomically: false, encoding: String.Encoding.utf8)
                }
                catch {print("Cant write data to IrEngines.txt")}
                }
            }
    
    
}

