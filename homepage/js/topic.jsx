import PropTypes from 'prop-types';
import React from 'react'
import Image from './Image';
import Story from './Story';

class Topic extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const {
      content,
      setTopicFocus,
      topicIdx,
      maxTopicIdx,
    } = this.props;

    const topicName = content?.name;

    console.log(content);

    // sort content by topicOrder
    const sortedStories = content?.stories.sort((a, b) => a.topicOrder - b.topicOrder);


    return (
      <div className='topic'>
        <h1>{topicName}</h1>
        {
          sortedStories?.map((story, i) => {
            return(story.type === "media" ? <Image id={story.uuid} keyNum={i} /> : <Story text={story.text} keyNum={i} /> )
          })
        }
        {
          topicIdx === 0 ? null : (
            <button onClick={() => { setTopicFocus(topicIdx - 1) }}>&lt;-</button>
          )
        }
        {
          topicIdx === maxTopicIdx ? null : (
            <button onClick={() => { setTopicFocus(topicIdx + 1) }}>-&gt;</button>
          )
        }
      </div>
    );
  }
}

Topic.propTypes = {
  // prop types go here
  content: PropTypes.object,
  topicIdx: PropTypes.number.isRequired,
  maxTopicIdx: PropTypes.number.isRequired,

  // methods:
  // setTopicFocus
};

Topic.defaultProps = {
  // default prop values go here if not required
};

export default Topic

