import React from 'react'

class CreatePage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      title: props.title,
      description: props.description,
      pageSize: props.pageSize,
      isOpen: false
    };
    this.setOpen = this.setOpen.bind(this);
    this.handleEntryChange = this.handleEntryChange.bind(this);
  }

  setOpen(event, b) {
    console.log(event);
    this.setState({ isOpen: b });
  }

  handleEntryChange(event, key) {
    const stagedEntries = this.state;
    stagedEntries[key] = event.target.value;
    this.setState({ stagedEntries });
  }

  render() {
    const stagedEntries = this.state;
    return (
      <div className="item-card-1" onClick={(event) => this.setOpen(event, true)}>
        <div className="item-card-content">
          {
            stagedEntries.isOpen? (
              <form>
                <input type="text" onChange={(event) => this.handleEntryChange(event, 'title')} value={stagedEntries.title} />
                <br />
                <input type="text" onChange={(event) => this.handleEntryChange(event, 'description')} value={stagedEntries.description} />
                <br />
                <input type="radio" id="size1" name="size" />
                <label htmlFor="size1"> Small </label><br />
                <input type="radio" id="size4" name="size" />
                <label htmlFor="size4"> Large </label><br />
                <input type="button" onSubmit={(event) => this.setOpen(event, false)} value="cancel" />
              </form>
            ) : (
              <h1>{stagedEntries.title}</h1>
              )
            }
        </div>
      </div>
    );
  }
}

CreatePage.propTypes = {
  // prop types go here
};

CreatePage.defaultProps = {
  // default prop values go here if not required
  title: "Create a new page...",
  description: "description (optional)",
  pageSize: 1
};

export default CreatePage
