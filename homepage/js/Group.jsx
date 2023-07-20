import PropTypes from 'prop-types';
import React from 'react'
import Image from './Image';
import Story from './Story';

class Group extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      name: "",
      stories: [],
      groupOrder: 0,
      fadeIn: false,
    };
  }

  componentDidMount() {
    const { content } = this.props;
    const { name, stories, groupOrder } = content;
    const sortedStories = stories.sort((a, b) => a.storyOrder - b.storyOrder);
    this.setState({ name: name, stories: sortedStories, groupOrder: groupOrder });
    setTimeout(() => {
      this.setState({ fadeIn: true });
    }, 100);
  }

  render() {
    const { name, stories, groupOrder, fadeIn } = this.state;
    const { transitionDirection } = this.props;
    return (
      <div className={`group ${fadeIn ? 'fade-in' : `fade-out slide-${transitionDirection}`}`} key={groupOrder}>
        <h1>{name}</h1>
        <div className='stories'>
          {
            stories.map((story, i) => {
              return (story.type === "media" ? <Image id={story.uuid} keyNum={i} /> : <Story text={story.text} keyNum={i} />)
            })
          }
        </div>
      </div>
    );
  }
}

Group.propTypes = {
  // prop types go here
  content: PropTypes.instanceOf(Object).isRequired,
  transitionDirection: PropTypes.string.isRequired,
};

Group.defaultProps = {
  // default prop values go here if not required
};

export default Group
