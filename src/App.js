import React, {useEffect , useState} from 'react';
import ReactDOM from 'react-dom/client';

const root = ReactDOM.createroot(document.getElementById("root"));

function ImageRef(props){
    return(
        <img className="ImageRef"
            src = {props.compart.imageUrl}
            alt = {props.compart.name}
        />
    );
}

function WebsiteHead(props) {
    return(
        <div className="WebsiteHead">
            <ImageRef compart = {props.compart}/>
            <div className = "WebsiteHead-name">
                {props.compart.name}
            </div>
            <head>{props.compart.head}</head>
            <div className = "WebsiteHead-version">
                {props.compart.version}
            </div>
        </div>
    );
}

function SettingsToggle(props) {
    const [count, setCount] = useState(0);
    useEffect(() => {
        console.log = 'SettingsToggle clicked ${count} times';
    });

    const [isTrue, setTrue] = useState(null);
    useEffect(() => {
        Settings.setTrue(props.compart.sett,handleStatusChange)
        return() => {
            Settings.setFalse(props.compart.sett,handleStatusChange);
        };
    });

    function handleStatusChange(status){
        setTrue(status.isTrue)
    }
}

function Settings(props){
    
}