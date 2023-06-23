import React from 'react'
import Picker from './picker';
import Topic from './topic';
import { render } from 'react-dom';

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
    };

    this.setTopicFocus = this.setTopicFocus.bind(this);
  }

  componentDidMount() {
    // fetch all the thumbnails, set state
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
          maxTopicIdx: data.topics.length - 1,
        });
      })
      .catch((error) => console.log(error));
  }

  setTopicFocus(topicIdx) {
    this.setState({ focusedTopicIdx: topicIdx });
  }

  render() {
    const {
      logname,
      topics,
      focusedTopicIdx,
      maxTopicIdx,
    } = this.state;
    const keys = Object.keys(topics);
    const focusedTopic = topics[keys[focusedTopicIdx]];

    const pickerPairs = keys.map((topicId, i) => { return ({ idx: i, name: topics[topicId].name }); });

    return (
      <div className='site'>
        <div className='topic-tray'>
          <Picker setTopicFocus={this.setTopicFocus} topics={pickerPairs} />
          <Topic setTopicFocus={this.setTopicFocus} content={focusedTopic} topicIdx={focusedTopicIdx} maxTopicIdx={maxTopicIdx} />
        </div>
      </div>
    );
  }
}

render(
  <Homepage />,
  document.getElementById('reactEntry'),
);