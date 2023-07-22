import React from 'react'
import Picker from './Picker';
import Topic from './Topic';
import { createRoot } from 'react-dom/client';
import Headbar from './Headbar';
import Footbar from './Footbar';
import { BrowserView, MobileView } from 'react-device-detect';
import MobilePage from './MobilePage';
import SplashPage from './SplashPage';

class Homepage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      logname: "",
      // list of objects, each has props for a topic
      topics: [],
      focusedTopicIdx: 0,
      maxTopicIdx: 0,
      launched: false,
      fadeIn: false,
    };

    this.setTopicFocus = this.setTopicFocus.bind(this);
    this.loadSite = this.loadSite.bind(this);
  }

  componentDidMount() {
    // fetch all the thumbnails, set state
    setTimeout(() => {
      this.setState({ fadeIn: true });
    }, 300)
    fetch("/api/v1/home/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        console.log(data);
        this.setState({
          logname: data.logname,
          topics: data.topics,
          maxTopicIdx: Object.keys(data.topics).length - 1,
          topicSwitches: 0  // for re-rendering after pickers
        });
      })
      .catch((error) => console.log(error));
  }

  loadSite() {
    // fade out after 400ms
    setTimeout(() => {
      this.setState({ fadeIn: false });
    }, 400);
    // change content 200ms later
    setTimeout(() => {
      this.setState({ launched: true });
    }, 600);
    // fade in 200ms after that
    setTimeout(() => {
      this.setState({ fadeIn: true });
    }, 800);
  }

  setTopicFocus(topicIdx) {
    const { topicSwitches } = this.state;
    this.setState({ focusedTopicIdx: topicIdx, topicSwitches: topicSwitches + 1 });
  }

  render() {
    const {
      logname,
      topics,
      focusedTopicIdx,
      topicSwitches,
      launched,
      fadeIn,
    } = this.state;
    const keys = Object.keys(topics);
    const focusedKey = keys[focusedTopicIdx];
    const focusedTopic = topics[focusedKey];

    const pickerTopics = keys.map((topicId, i) => { return ({ idx: i, name: topics[topicId].name, icon: topics[topicId].icon }); });

    return (
      <div className={`site fade-${fadeIn ? 'in' : 'out'}`}>
        <BrowserView>
          {
            launched ? (
              <>
                <div className='static-navigator'>
                  <Headbar />
                  <Picker setTopicFocus={this.setTopicFocus} topics={pickerTopics} />
                </div>
                <div className='topic-tray' key={`${focusedKey}-${topicSwitches}`}>
                  {
                    focusedTopic ? <Topic content={focusedTopic} topicIdx={focusedTopicIdx} /> : null
                  }
                </div>
                <Footbar />
              </>
            ) : (
              <SplashPage loadSite={this.loadSite} />
            )
          }
        </BrowserView>
        <MobileView>
          <MobilePage />
        </MobileView>
      </div>
    );
  }
}

const container = document.getElementById('reactEntry');
const root = createRoot(container);
root.render(<Homepage />);
